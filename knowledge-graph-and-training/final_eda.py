import pandas as pd
import matplotlib.pyplot as plt

# Load the final cleaned dataset
df = pd.read_csv('final_cleaned_dataset.csv')

print(f"✅ Total assessments: {len(df)}\n")

# How many unique competencies?
all_competencies = df['Competencies'].apply(eval)  # Convert string to list
flat_list = [item for sublist in all_competencies for item in sublist]
unique_competencies = set(flat_list)

print(f"✅ Unique competencies: {len(unique_competencies)}")
print(f"✅ Top 10 most common competencies:")

# Count frequency
from collections import Counter
counter = Counter(flat_list)
for competency, count in counter.most_common(10):
    print(f"{competency}: {count}")

# Plot Top 10
top_10 = counter.most_common(10)
competencies, counts = zip(*top_10)

plt.figure(figsize=(10,6))
plt.barh(competencies, counts, color='skyblue')
plt.gca().invert_yaxis()
plt.title('Top 10 Most Common Competencies')
plt.xlabel('Frequency')
plt.show()
