import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ast

# Load data
df = pd.read_csv('cleaned_data.csv')
df = df.dropna(subset=['Title'])

# Create Graph
G = nx.Graph()

for idx, row in df.iterrows():
    title = row['Title']
    competencies = ast.literal_eval(row['Competencies']) if pd.notna(row['Competencies']) else []
    G.add_node(title, type='assessment')
    for competency in competencies:
        G.add_node(competency, type='competency')
        G.add_edge(title, competency)

# Layout
pos = nx.kamada_kawai_layout(G)  # <- Better layout for separation

# Node colors and sizes
node_colors = ['skyblue' if G.nodes[node]['type'] == 'assessment' else 'lightgreen' for node in G.nodes]
node_sizes = [3000 if G.nodes[node]['type'] == 'assessment' else 2000 for node in G.nodes]

# Draw
plt.figure(figsize=(28, 20))  # Bigger figure
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.4, width=1.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")

plt.title("Knowledge Graph: Assessments and Competencies", fontsize=22)
plt.axis('off')
plt.show()
