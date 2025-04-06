# eda.py

import pandas as pd
import ast
from collections import Counter

# Load the cleaned dataset
df = pd.read_csv('final_cleaned_dataset.csv')

# ------- 1. Basic Information -------
print(f"\nTotal number of assessments: {len(df)}")

# ------- 2. Competency Analysis -------
competency_list = []

for comp_list in df['Competencies']:
    if pd.notna(comp_list):
        if isinstance(comp_list, str):
            # Convert string representation of list to actual list
            comp_list = ast.literal_eval(comp_list)
        competency_list.extend(comp_list)

# Count occurrences
competency_counter = Counter(competency_list)

print("\nTop 10 Most Common Competencies:")
for competency, count in competency_counter.most_common(10):
    print(f"{competency}: {count}")

# ------- 3. Missing Data Check -------
missing_data = df.isnull().sum()
print(f"\nMissing data per column:\n{missing_data}")

# ------- 4. Sample Data -------
print("\nSample data:")
print(df.head())

import matplotlib.pyplot as plt

# Plot Top 10 Competencies
top_10 = competency_counter.most_common(10)
competencies, counts = zip(*top_10)

plt.figure(figsize=(10,5))
plt.barh(competencies, counts, color='skyblue')
plt.xlabel('Number of Assessments')
plt.title('Top 10 Most Common Competencies')
plt.gca().invert_yaxis()
plt.show()

