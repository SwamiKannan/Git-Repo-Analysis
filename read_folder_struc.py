import pickle
import networkx as nx
import matplotlib.pyplot as plt

from stdlib_list import stdlib_list
libraries=stdlib_list("3.9")


with open('folder_struct','rb') as p:
    read_struc=pickle.load(p)

dict_libraries={}
for keys, values in read_struc.items():
    file1=read_struc[keys]
    for import1 in file1:
        libs=import1.split(' ')[1]
        if libs in libraries or libs=='':
            continue
        if libs.find('.')>0:
            libs=libs.split('.')[0]
        if keys in dict_libraries:
            dict_libraries[keys].append(libs)
        else:
            dict_libraries[keys]=[libs]
    dict_libraries={k:set(v) for k,v in dict_libraries.items()}
# print(dict_libraries)

# nodes=[]
# connections={}
# for k,v in dict_libraries.items():
#     key_nodes=k.split('\\')[-1][:-3]
#     nodes+=[key_nodes]+list(v)
#     if key_nodes in connections:
#         connections[key_nodes].append(list(v))
#     else:
#         connections[key_nodes]=[v]
# print(nodes)
# print('\n')
# print(connections)

G=nx.DiGraph(directed=True)
from_nodes=[]
to_nodes=[]

for key, values in dict_libraries.items():
        # print(key,values)
        key=key.split('\\')[-1][:-3]
        for v in values:
            from_nodes.append(key)
            to_nodes.append(v)

# print('to_nodes\n',to_nodes)
# print('from_nodes\n',from_nodes)





for i in range(len(set(from_nodes+to_nodes))):
    G.add_node(list(set(from_nodes+to_nodes))[i])
for i in range(len(to_nodes)):
    G.add_edges_from([(to_nodes[i], list(from_nodes)[i])])

node_setup = {node:[G.in_degree(node),G.out_degree(node)] for node in G.nodes}
only_calling = {node:[G.in_degree(node),G.out_degree(node)] for node in G.nodes if G.out_degree(node)==0}
only_called = {node:[G.in_degree(node),G.out_degree(node)] for node in G.nodes if G.in_degree(node)==0}
# print(only_called)
# print(only_calling)
print('Functions that are only called')
print('{:>12}  {:>12} '.format('Functions', 'No. of times called'))
for key, values in only_called.items():
    print('{:>12}  {:>12} '.format(key, values[1]))

print('\n')
print('\n')
max_val=max(only_called.values())[1]
max_called_function=[key for key,value in only_called.items() if value[1]==max_val]
print('Function that is called maximum number of times')
for i in max_called_function:
    print('{:>12}  {:>12} '.format(i, max_val))
    # print(f'{i}:{max_val}')
print('\n')

print('Functions that are only calling other functions')
for key, values in only_calling.items():
    print('{:>20}  {:>20} '.format(key, values[0]))
print('\n')
max_val=max(only_calling.values())[0]
max_called_function=[key for key,value in only_calling.items() if value[0]==max_val]
print('Function that calls the maximum number of other functions')
for i in max_called_function:
    print('{:>12}  {:>12} '.format(i, max_val))

options = {
    'with_labels':True,
    'node_color': 'red',     # color of node
    'node_size': 50,          # size of node
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 18,            # size of arrow
    'edge_color':'#ECECEC',        # edge color
    'font_size':10,
    'arrows':10,
    'font_color':'black'
}

def nudge_labels(pos, x_shift=5,y_shift=5):
    return {n:(x+x_shift,y+y_shift) for n,(x,y) in pos.items()}

pos = nx.circular_layout(G)
pos_nodes=nudge_labels(pos)

plt.figure(figsize=(12,15))
ax = plt.gca()
ax.set_title('Graph analysis of repo')
nx.draw(G,pos,**options,verticalalignment='bottom',horizontalalignment='left')
# nx.draw_networkx_labels(G,pos=pos_nodes,ax=ax)
ax.set_ylim(tuple(i*1.1 for i in ax.get_ylim()))  
plt.show()

# pos = nx.spring_layout(G, k=0.5, iterations=100)
# for n, p in pos.items():
#     G.nodes[n]['pos'] = p
       

# # for key,values in read_struc.items():
# #    for v in values:
# #     if v.split(' ')[0]=='import':
# #         print(key, values)
# #         break
# #     break