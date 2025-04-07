# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and vectorizer
model = joblib.load('knowledge-graph-and-training/assessment_recommender_model.pkl')
vectorizer = joblib.load('knowledge-graph-and-training/competency_vectorizer.pkl')

# Load final dataset
df = pd.read_csv('knowledge-graph-and-training/final_cleaned_dataset.csv')

# Streamlit UI
st.title("Assessment Recommendation System")
st.write("Enter the competencies you want to assess:")

user_input = st.text_input("Enter competencies separated by commas (e.g., Problem Solving, Sales Skills)")

if st.button("Recommend Assessments"):
    if user_input:
        competencies = [comp.strip() for comp in user_input.split(',')]
        
        input_vector = vectorizer.transform([competencies])  # <-- No join(), pass list inside list
        
        distances, indices = model.kneighbors(input_vector, n_neighbors=5)
        
        recommended_assessments = df.iloc[indices[0]]['Title'].tolist()
        
        st.subheader("Recommended Assessments:")
        for assessment in recommended_assessments:
            st.write("- ", assessment)
    else:
        st.warning("Please enter some competencies!")
