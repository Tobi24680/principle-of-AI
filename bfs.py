#bfs program
def bfs(graph,start):
   
    visited.add(start)
    queue.append(start)
    while queue:
        node=queue.pop(0)
        print(node,end='')
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                
if __name__=='__main__':
 graph={
        0:[1,2],
        1:[2],
        2:[0,3],
        3:[3]
          }
visited=set()
queue=[]
print("bfs:")
bfs(graph,0)