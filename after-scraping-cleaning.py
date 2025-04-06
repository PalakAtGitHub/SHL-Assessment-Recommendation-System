import pandas as pd

competency_map = {
    'A': 'Attention to Detail',
    'B': 'Business Communication',
    'C': 'Critical Thinking',
    'D': 'Data Interpretation',
    'E': 'Emotional Intelligence',
    'F': 'Financial Acumen',
    'G': 'Global Awareness',
    'H': 'Hiring Skills',
    'I': 'Innovation',
    'J': 'Judgment and Decision Making',
    'K': 'Knowledge of Subject',
    'L': 'Leadership',
    'M': 'Motivation',
    'N': 'Negotiation Skills',
    'O': 'Organizational Skills',
    'P': 'Problem Solving',
    'Q': 'Quality Focus',
    'R': 'Risk Management',
    'S': 'Sales Skills',
    'T': 'Teamwork',
    'U': 'Understanding Customer Needs',
    'V': 'Verbal Communication',
    'W': 'Work Ethic'
}

def clean_competencies(comp_list_str):
    """
    Clean and map competencies from a messy string format to a list of full competency names.
    """
    if not isinstance(comp_list_str, str) or comp_list_str.strip() in ('[]', ''):
        return []  

    comp_list_str = comp_list_str.strip("[]'\"")
    
    codes = comp_list_str.split('\\n')
    
    mapped = [competency_map.get(code.strip(), code.strip()) for code in codes if code.strip()]
    
    return mapped

df = pd.read_csv('shl_catalog.csv')   # <-- Change filename if needed

df['Competencies'] = df['Competencies'].apply(clean_competencies)

df = df.dropna(subset=['Title', 'Link'])

df = df.reset_index(drop=True)

df.to_csv('cleaned_data.csv', index=False)

print(df.head(10))
