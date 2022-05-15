graph = input()

graph = graph.replace('XXXX', 'AAAA')
graph = graph.replace('XX', 'BB')

if 'X' in graph:
    print(-1)
else:
    print(graph)