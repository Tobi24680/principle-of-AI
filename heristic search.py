import heapq
grid=[[0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,0,0,1],
      [0,1,1,0,0],
      [0,0,0,0,0]]
start=(0,0)
goal=(4,4)
def h(node,goal):
    return abs(node[0]-goal[0]) + abs(node[1]-goal[1])
def astar(grid,start,goal):
    open_list=[(0,start)]
    came={}
    g={(x,y): float('inf') for x in range(len(grid)) for y in range(len(grid[0]))}
    g[start]=0
    f={node:float('inf') for node in g}
    f[start]=h(start,goal)
    while open_list:
        _,current=heapq.heappop(open_list)
        if current==goal:
            path=[]
            while current in came:
                path.append(current)
                current=came[current]
            return path[::-1]
        for n in[(0,1),(0,-1),(1,0),(-1,0)]:
            x,y=current[0]+n[0],current[1]+n[1]
            if 0<=x<len(grid) and 0<y<len(grid[0]) and grid[x][y]==0:
                tg=g[current]+1
                if tg<g[(x,y)]:                    
                    came[(x,y)]=current
                    g[(x,y)]=tg
                    f[(x,y)]=tg+h((x,y),goal)
                    heapq.heappush(open_list,(f[(x,y)],(x,y)))
    return None
path=astar(grid,start,goal)
print(path)

 