#dfs program
def dfs(graph,start,visited):
    if start not in visited:
        print(start,end='')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph,neighbor,visited)
            
if __name__=='__main__':
  graph=  {
           'a':['b','c'],
           'b':['a','d','e'],
            'c':['a','f'],
            "d":['b'],
            'e':['b','f'],
            'f':['c','e'],
                 }
                 
visited=set()
print('dfs start from vertex a:')
dfs(graph,'d',visited)