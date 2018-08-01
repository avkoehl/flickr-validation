import json
import networkx as nx
import community
import matplotlib.pyplot as plt

f = open ("./new_binary_results.csv")
G = nx.Graph()


def parse( line ):
    line = line.rstrip()
    elements = line.split(',')
    
    # get source
    source = elements[0].split(' ')[0]

    # get targets and weights
    targets = []
    for element in elements[2:]:
        targets.append(element)

    return (source, targets)

## MAIN 
nodes = []
links = []
for n, line in enumerate(f):
    node = {}
    link = {}

    source,targets = parse(line)
    node["name"] = source
    nodes.append(node.copy())
    G.add_node(source)

    for t in targets:
        exploded = t.split(' ')
        distance = 1 / (1 + float(exploded[1]))
        edge = exploded[0]
        link["source"] = source
        link["target"] = edge
        link["weight"] = distance
        if (distance < 1/ 1 + 6):
            G.add_edge(source, edge, weight=distance)
            links.append(link.copy())


partition = community.best_partition(G)
for com in set(partition.values()) :
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    print (com, list_nodes)

#drawing
#size = float(len(set(partition.values())))
#pos = nx.spring_layout(G)
#count = 0.
#for com in set(partition.values()) :
#    count = count + 1.
#    list_nodes = [nodes for nodes in partition.keys()
                                #if partition[nodes] == com]
    #nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
    #                            node_color = str(count / size))
#    print (list_nodes)


#plt.show()

