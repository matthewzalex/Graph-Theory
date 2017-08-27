from graphviz import Graph

dot = Graph(comment='Graph')


n = input("Enter no.of Edges : ")
for i in range(0,n):
    edge = raw_input().split(' ')
    dot.edge(edge[0],edge[1],label=edge[2])

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
dot.save('file.gv')
dot.render('file.gv', view=True)


'''Sample Input

Enter no.of Edges : 5
1 1 a
1 2 b
1 2 c
2 3 d
1 3 e

'''