class Node:
    def __init__(self,name):
        self.name=name
        self.edges=[]
    def add_edge(self,relation,node):
        self.edges.append((relation,node))
    def __str__(self):
        return self.name
class semantic_network:
    def __init__(self):
        self.nodes=[]
    def add_nodes(self,name):
        node = Node(name)
        self.nodes.append(node)
        return node
    def __str__(self):
        result='sementic network\n'
        for node in self.nodes:
            result+=f'{node}has relation:\n'
            for relation , related_node in node.edges:
                result+=f'{relation}:{related_node}\n'
        return result
semantic_net=semantic_network()
while True:
    print('1.add node')
    print('2.add relation')
    print('3.exit')
    choice=input("enter your choice")
    if choice=='1':
        node_name=input('enter node name')
        semantic_net.add_nodes(node_name)
        print(f'node{node_name}added')
    elif choice=='2':
        node_name=input("enter node name")
        relation=input("enter relation")
        related_node_name=input('enter related node name')
        node=next((n for n in semantic_net.nodes if n.name==node_name),None)
        related_node=next((n for n in  semantic_net.nodes if n.name==related_node_name),None)
        if node and related_node:
            node.add_edge(relation,related_node)
            print(f'relation added:{node_name}_{relation}_{related_node_name}')
        else:
            print("one or both nodes not found")
    else :
        break
print(semantic_net)