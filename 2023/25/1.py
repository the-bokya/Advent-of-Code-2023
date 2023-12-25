from itertools import combinations
import networkx as nx
conns = []
G = nx.Graph()
while True:
    try:
        a, bs = input().split(": ")
        bs = bs.split(" ")
        for b in bs:
            G.add_edge(a, b, capacity=1)
    except Exception as e:
        print(e)
        break


count = 0
for a, b in list(combinations(G.nodes, 2)):
    cut_val, partition = nx.minimum_cut(G, a, b)
    if cut_val == 3:
        print(len(partition[0]) * len(partition[1]))
        break


