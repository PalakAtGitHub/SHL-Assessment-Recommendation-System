from collections import Counter
import ast
import pandas as pd

df = pd.read_csv('cleaned_data.csv')

num_assessments = len(df)
print(f'Total number of assessments: {num_assessments}')

competency_list = []

for comp in df['Competencies']:
    if pd.notna(comp):
        comp_eval = ast.literal_eval(comp)
        competency_list.extend(comp_eval)

# Count the occurrences of each competency
competency_counter = Counter(competency_list)

# Task 3: Display the most common competencies
print("Top 10 most common competencies:")
for competency, count in competency_counter.most_common(10):
    print(f'{competency}: {count}')

# Task 4: Check for missing or unusual values
missing_data = df.isnull().sum()
print(f"\nMissing data per column:\n{missing_data}")

# Task 5: Check the first few rows of the cleaned dataset
print("\nSample data:")
print(df.head())
