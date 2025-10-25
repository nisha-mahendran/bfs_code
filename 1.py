import cv2 #for image processing
from collections import deque #deque(double ended queue) for BFS
import numpy as np #perform some calculations 

img=cv2.imread("m.png") #reads image into array
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to grayscale
_,mask = cv2.threshold(gray,100,255,cv2.THRESH_BINARY) # if pixels are above 100 set to 255(white) else 0(black)
occupancy_grid = (255 - mask) // 255 #question
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # hue saturation value easier for color filtering
lower_green = np.array([40, 50, 50]) #(min hue,min sat,min val)
upper_green = np.array([80, 255, 255]) #(max ")
mask_a = cv2.inRange(hsv, lower_green, upper_green) #creates mask by changing the pixels in range to white and rest to black
green_pixels = np.argwhere(mask_a == 255) # gets coordinates of green(white) pixels
start_point = tuple(map(int,green_pixels[0])) # first green pixel as start point
lower_blue = np.array([90, 50, 50]) #same
upper_blue = np.array([130, 255, 255])
mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
blue_pixels = np.argwhere(mask_b == 255)
end_point = tuple(map(int,blue_pixels[0])) 
print(start_point,end_point)
for px, py in green_pixels:
    occupancy_grid[px, py] = 0  # mark whole green region as free

for px, py in blue_pixels:
    occupancy_grid[px, py] = 0  # same
queue = deque()
queue.append(start_point)
visited=set() # set because we only want unique nodes
visited.add(start_point)
parent={}
parent[start_point] = None

direction=[(1,0),(-1,0),(0,1),(0,-1)]
n=0
end_region = {tuple(map(int, px)) for px in blue_pixels}
rows, cols = occupancy_grid.shape
while queue:
    node = queue.popleft()
    x,y = node

    if node in end_region:
        found_end = node
        break
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0<=nx<rows and 0 <=ny<cols and (nx,ny) not in visited and occupancy_grid[nx,ny] == 0:
            visited.add((nx,ny))
            queue.append((nx,ny))
            parent[(nx,ny)]=(x,y)
            n+=1
path=[]
while node != start_point:
    path.append(node)
    node=parent[node]
path.append(start_point)
path.reverse()

for i in range(len(path)-1): # why -1? to define i+1
    p1 = (int(path[i][1]), int(path[i][0])) #path[i] represents (row, col) which is (y,x) and path[i][0] is y and path[i][1] is x
    p2 = (int(path[i+1][1]), int(path[i+1][0]))
    cv2.line(img, p1, p2, (0, 0, 255), 2) #(image to draw line,starting point of line,ending point of line,red line,thickness)

print("path length : " , len(path))
print("number of nodes explored: ", n)
cv2.imshow("path",img)
cv2.waitKey()
cv2.destroyAllWindows()
