
import networkx as nx
import matplotlib.pyplot as plt
import json


class GraphAnalysis():
    def __init__(self, gh_lib, write=True):
        self.G=nx.DiGraph(directed=True)
        self.from_nodes=[]
        self.to_nodes=[]
        self.lib=gh_lib.dict_libraries
        self.write=write

    def get_nodes(self):
        for key, values in self.lib.items():
            key=key.split('\\')[-1][:-3]
            for v in values:
                self.from_nodes.append(key)
                self.to_nodes.append(v)

    def create_graph(self):
        '''
        Graph analysis of the dictionary
        Create a  graphs with (from_nodes, to_nodes) as edges and the set of [from_nodes]+[to_nodes] as nodes
        '''
        for i in range(len(set(self.from_nodes+self.to_nodes))):
            self.G.add_node(list(set(self.from_nodes+self.to_nodes))[i])
        for i in range(len(self.to_nodes)):
            self.G.add_edges_from([(self.to_nodes[i], list(self.from_nodes)[i])])

    def analyze_graph(self):
        '''
        Graph analysis of the dictionary
        Identify the following:
        1. All nodes with only incoming edges (only called functions never calling functions - indicating that they could be the core library / external libraries)
        2. Node with maximum called edges (implies that this might be the core library)
        3. All nodes with only outgoing edges (only calling functions never called functions - indicating that they might be more higher order libraries or .py files)
        4. Node with maximum calling edges (implies that this might be the highest level library / .py file)
        '''
        node_setup = {node:[self.G.in_degree(node),self.G.out_degree(node)] for node in self.G.nodes}
        only_calling = {node:[self.G.in_degree(node),self.G.out_degree(node)] for node in self.G.nodes if self.G.out_degree(node)==0}
        only_called = {node:[self.G.in_degree(node),self.G.out_degree(node)] for node in self.G.nodes if self.G.in_degree(node)==0}

        if self.write:
            with open('only_calling.json','w') as f:
                json.dump(only_calling,f,indent=4)
            with open('only_called.json','w') as f:
                json.dump(only_called,f,indent=4)

        #******** Only called functions*********#
        print('Functions that are only called')
        print('{:>12}  {:>12} '.format('Functions', 'No. of times called'))
        for key, values in only_called.items():
            print('{:>12}  {:>12} '.format(key, values[1]))
        print('\n\n')
        #******** Max called functions *********#
        max_val=max(only_called.values())[1]
        max_called_function=[key for key,value in only_called.items() if value[1]==max_val]
        print('Function that is called maximum number of times')
        for i in max_called_function:
            print('{:>12}  {:>12} '.format(i, max_val))
        print('\n\n')
        
        #******** Only calling functions*********#
        print('Functions that are only calling other functions')
        for key, values in only_calling.items():
            print('{:>20}  {:>20} '.format(key, values[0]))
        print('\n\n')
        #******** Max calling functions *********#
        max_val=max(only_calling.values())[0]
        max_called_function=[key for key,value in only_calling.items() if value[0]==max_val]
        print('Function that calls the maximum number of other functions')
        for i in max_called_function:
            print('{:>12}  {:>12} '.format(i, max_val))

    def visualize_graph(self):
        '''
        Graph analysis of the dictionary
        Charting the graph
        1. Drawing the chart of all nodes and edges using matplotlib

        '''

        formatting = {
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

        self.pos = nx.circular_layout(self.G)

        plt.figure(figsize=(12,15))
        ax = plt.gca()
        ax.set_title('Graph analysis of repo')
        nx.draw(self.G,self.pos, **formatting,verticalalignment='bottom',horizontalalignment='left')
        ax.set_ylim(tuple(i*1.1 for i in ax.get_ylim())) 
        if self.write:
            plt.savefig('graph.jpg',format='jpg',dpi=300) 
        plt.show()
        
    
    def final_analysis(self):
        self.get_nodes()
        self.create_graph()
        self.analyze_graph()
        self.visualize_graph()

    def analyze(self):
        self.final_analysis()