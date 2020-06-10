#task2b_lab4
graph = {'A': ['B', 'D'],
        'B': ['C', 'E'],
        'D': ['E', 'G','H'],
        'E' : ['C', 'F'],
        'G' : ['H']}
def dfs(graph,start,end):
    stack=[]
    stack.append(start)
    while(stack):
        path=stack.pop()
        node=path[-1]
        if node==end:
            return path
        for every_successor in graph.get(node,[]):
            new_path=list(path)
            new_path.append(every_successor)
            stack.append(new_path)
    return 'Failure'

print(dfs(graph,'A','G'))