from time import process_time
import networkx as nx
import matplotlib.pyplot as plt


graph = {
        'D':['B', 'E'], 'B':['A','C'], 'E':['F'], 'F':[], 'A':[], 'C':[]  #dbacef

}

graph1 = {
        'D':['B', 'E'], 'B':['A','C'], 'E':['F'], 'F':[], 'A':['S', 'Z'], 'S':['N'], 'Z':[], 'N':[], 'C':[]  #dbacef

}



def dfs (visited1, graph, root):
    if root not in visited1:
        print (root, end = " ") 
        visited1.add(root)
        for neighbour in graph[root]:
            dfs(visited1, graph, neighbour)

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)



# Driver Code
times=[]
visited1=set()
visited=[]
queue=[]
print('Balanced:')
print("Following is the Depth-First Search")
start = process_time()
dfs(visited1, graph, 'D')
end = process_time()
times.append(end)
print(",Time is ",end, end = " ")
print()


print("Following is the Breadth-First Search")
start = process_time()
bfs(visited, graph, 'D')
end = process_time()
times.append(end)
print(",Time is ",end, end = " ")
print()



visited1=set()
visited=[]
queue=[]

print('Unbalanced:')
print("Following is the Depth-First Search")
start = process_time()
dfs(visited1, graph1, 'D')
end = process_time()
times.append(end)
print(",Time is ",end, end = " ")

print()
print("Following is the Breadth-First Search")
start = process_time()
bfs(visited, graph1, 'D')
end = process_time()
times.append(end)
print(",Time is ",end, end = " ")
print()


print("The following processing times outputs:")
print(times)
print(min(times))
print("Index of min processing time:")
print(times.index(min(times)))




# Create a new undirected graph
G = nx.Graph()
# Add nodes to the graph
for node in graph:
    G.add_node(node)

# Add edges to the graph
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)
labels = {}
labels['D'] = 'root'


# Draw the graph using matplotlib
pos = nx.spring_layout(G) # define the layout of the nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='red') # draw nodes
nx.draw_networkx_edges(G, pos) # draw edges
nx.draw_networkx_labels(G, pos, font_size=20, font_family='monospace') # draw labels
x, y = pos['D']
plt.text(x, y+0.1, 'Root', horizontalalignment='center', fontweight='bold')
# Display the graph
plt.xlabel('Balanced tree input,no.1')
plt.grid()
plt.show()



# Create an empty graph object
G = nx.Graph()

# Add nodes to the graph
for node in graph1:
    G.add_node(node)

# Add edges to the graph
for node in graph1:
    for neighbor in graph1[node]:
        G.add_edge(node, neighbor)

labels = {}
labels['D'] = 'root'
# Draw the graph using matplotlib
pos = nx.spring_layout(G) # define the layout of the nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='red') # draw nodes
nx.draw_networkx_edges(G, pos) # draw edges
nx.draw_networkx_labels(G, pos, font_size=20, font_family='monospace') # draw labels
x, y = pos['D']
plt.text(x, y+0.1, 'Root', horizontalalignment='center', fontweight='bold')
plt.xlabel('Unbalanced tree,input no.2')
plt.grid()
plt.show()