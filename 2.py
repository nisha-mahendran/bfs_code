from collections import deque

adj = [list(map(int, input().split())) for _ in range(5)]
queue = deque()
queue.append(0)
visited=set() 
visited.add(0)
bfs=[]

while queue:
    node = queue.popleft()
    bfs.append(node)
    for i in adj[node]:
        if i not in visited :
            visited.add(i)
            queue.append(i)

print(bfs)
