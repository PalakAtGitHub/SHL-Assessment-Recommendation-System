# vectorization_and_training.py

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import ast

# Step 1: Load data
df = pd.read_csv('training_ready_dataset.csv')
df['Competencies'] = df['Competencies'].apply(ast.literal_eval)

# Step 2: Vectorize competencies
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['Competencies'])

# Step 3: Prepare labels (for now, we can predict assessment titles)
y = df['Title']

# Step 4: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a simple model
model = KNeighborsClassifier(n_neighbors=3)  # You can adjust neighbors
model.fit(X_train, y_train)

# Step 6: Save model and vectorizer
joblib.dump(model, 'assessment_recommender_model.pkl')
joblib.dump(mlb, 'competency_vectorizer.pkl')

print("✅ Model and vectorizer saved!")




import joblib

# Load model and vectorizer
model = joblib.load('assessment_recommender_model.pkl')
mlb = joblib.load('competency_vectorizer.pkl')

def recommend_assessments(user_competencies, top_n=5):
    # user_competencies: list of competencies input by user
    user_vec = mlb.transform([user_competencies])
    preds = model.kneighbors(user_vec, n_neighbors=top_n, return_distance=False)
    recommendations = y_train.iloc[preds[0]].tolist()
    return recommendations

# Example usage
user_input = ['Problem Solving', 'Critical Thinking']
print("Recommended Assessments:", recommend_assessments(user_input))
