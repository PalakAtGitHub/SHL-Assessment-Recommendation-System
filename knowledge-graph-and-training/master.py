# master.py

import pandas as pd
import ast

# Step 1: Load the cleaned dataset
df = pd.read_csv('final_cleaned_dataset.csv')

# Step 2: Convert competencies back from string to real list
df['Competencies'] = df['Competencies'].apply(ast.literal_eval)

# Step 3: Print basic info
print(f"✅ Loaded {len(df)} assessments.")

print("\n✅ Sample assessments and competencies:")
print(df.sample(5))

# Step 4: Save the final clean dataset
df.to_csv('training_ready_dataset.csv', index=False)
print("\n✅ Final training-ready dataset saved as 'training_ready_dataset.csv'.")

