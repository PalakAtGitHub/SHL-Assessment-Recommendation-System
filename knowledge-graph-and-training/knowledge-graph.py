# knowledge_graph.py

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ast

# Step 1: Load the training-ready dataset
df = pd.read_csv('training_ready_dataset.csv')
df['Competencies'] = df['Competencies'].apply(ast.literal_eval)

# Step 2: Initialize the graph
G = nx.Graph()

# Step 3: Add nodes and edges
for idx, row in df.iterrows():
    assessment = row['Title']
    competencies = row['Competencies']
    
    G.add_node(assessment, type='assessment')
    
    for comp in competencies:
        G.add_node(comp, type='competency')
        G.add_edge(assessment, comp)

print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Step 4: Save the graph (optional, if needed later)
nx.write_gpickle(G, "assessment_knowledge_graph.gpickle")
print("✅ Graph saved as 'assessment_knowledge_graph.gpickle'.")

# (Optional) Step 5: Visualize a small part of the graph
sample_nodes = list(df['Title'].sample(10))  # Random 10 assessments
subgraph = G.subgraph(sample_nodes + [n for a in sample_nodes for n in G.neighbors(a)])

plt.figure(figsize=(12,8))
pos = nx.spring_layout(subgraph, seed=42)
node_colors = ["lightblue" if G.nodes[n]['type'] == 'assessment' else "lightgreen" for n in subgraph.nodes()]
nx.draw(subgraph, pos, with_labels=True, node_color=node_colors, font_size=8)
plt.title("Sample Knowledge Graph View")
plt.show()
