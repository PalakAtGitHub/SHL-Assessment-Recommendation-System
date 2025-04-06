import pandas as pd

# Load the cleaned competency dataset
df = pd.read_csv('cleaned_competency_dataset.csv')

# Strip spaces and Title Case
df['Title'] = df['Title'].apply(lambda x: x.strip().title())
df['Competencies'] = df['Competencies'].apply(lambda x: x.strip().title())

# Drop exact duplicate rows
df = df.drop_duplicates()

# ------------------ FLAG suspicious titles (for info) ------------------ #

# Titles containing suspicious numbers
suspicious_numbers = ['10', '20', '80', '2013', '2014', '44', '45', '365']
pattern_numbers = '|'.join(suspicious_numbers)

titles_with_numbers = df[df['Title'].str.contains(pattern_numbers, na=False)]
print("\nTitles with suspicious numbers:")
print(titles_with_numbers['Title'])

# Titles containing weird special characters (+, %, *, etc.)
unwanted_special_chars = r'[+\*@#%&!$]'
titles_with_unwanted_chars = df[df['Title'].str.contains(unwanted_special_chars, regex=True, na=False)]
print("\nTitles with weird special characters:")
print(titles_with_unwanted_chars['Title'])

# ------------------ REMOVE unwanted titles ------------------ #

# Remove rows where title contains suspicious numbers
df = df[~df['Title'].str.contains(pattern_numbers, na=False)]

# Remove rows where title contains weird special characters
df = df[~df['Title'].str.contains(unwanted_special_chars, regex=True, na=False)]

# ------------------ Save final cleaned dataset ------------------ #

df.to_csv('final_cleaned_dataset.csv', index=False)
print(f"\n✅ Final cleaned dataset saved as 'final_cleaned_dataset.csv' with {len(df)} assessments.")
