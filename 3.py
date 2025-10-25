adj = [list(map(int, input().split())) for _ in range(5)]
stack=[]
visited=set() 
dfs=[]

def dfs_algo(v):
   stack.append(v)
   visited.add(v)
   dfs.append(v)
   for i in adj[v]:
      if i not in visited :
        dfs_algo(i)
   return dfs
dfs_algo(0)
print(dfs)
