
import pandas as pd
from graphviz import Digraph

# Load the data from the CSV file
df = pd.read_csv('Sample_Data.csv')

# Create a new directed graph
dot = Digraph()

# Dictionary to store created marriage nodes
marriage_nodes = {}

# Add nodes for each person
for index, row in df.iterrows():
    label = row['Name']
    additional_info = []
    if pd.notna(row['Born']):
        if pd.notna(row['Born_At']):
            additional_info.append(f"Born: {row['Born']}, {row['Born_At']}")
        else:
            additional_info.append(f"Born: {row['Born']}")
    if pd.notna(row['Died']):
        if pd.notna(row['Died_At']):
            additional_info.append(f"Died: {row['Died']}, {row['Died_At']}")
        else:
            additional_info.append(f"Died: {row['Died']}")
    if additional_info:
        label += '\n' + '\n'.join(additional_info)
    dot.node(f'P{row["ID"]}', label, shape='square', style='filled', fillcolor='lightblue', fontname='Arial', fontsize='20', fixedsize='true', width='3', height='3')

# Add marriage nodes and edges
for index, row in df.iterrows():
    if pd.notna(row['Married_To']) and f'M{min(row["ID"], int(row["Married_To"]))}{max(row["ID"], int(row["Married_To"]))}' not in marriage_nodes:
        marriage_node = f'M{min(row["ID"], int(row["Married_To"]))}{max(row["ID"], int(row["Married_To"]))}'
        label = ""
        if pd.notna(row['Married']):
            if pd.notna(row['Married_At']):
                label += f"Married: {row['Married']}, {row['Married_At']}"
            else:
                label += f"Married: {row['Married']}"
        dot.node(marriage_node, label, shape='ellipse', style='filled', fillcolor='lightgray', fontname='Arial', fontsize='20')
        dot.edge(f'P{row["ID"]}', marriage_node, dir='none')
        dot.edge(f'P{int(row["Married_To"])}', marriage_node, dir='none')
        marriage_nodes[marriage_node] = True
        
        # Add edge from marriage node to child
        if pd.notna(row['Parent_Of']):
            dot.edge(marriage_node, f'P{int(row["Parent_Of"])}')

# Render the graph
dot.render('family_tree', format='png', view=True)
