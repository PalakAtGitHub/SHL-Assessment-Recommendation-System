# SHL Assessment Recommender System

This project builds a **knowledge graph** and **recommendation system** for SHL assessments based on competencies. It covers the full pipeline from **web scraping** to **data cleaning**, **EDA**, and **model training**.

---

## 📂 Project Structure

```
SHL-Assess-Rec-System/
├── Web Scraping - Data Extraction/
│   ├── after-scraping-cleaning.py         # Clean raw scraped data
│   ├── cleaned_data.csv                   # Cleaned scraped data
│   ├── shl-scraping.py                   # Scrape SHL catalog
│   └── shl_catalog.csv                   # Raw scraped catalog
├── knowledge-graph-and-training/
│   ├── deep_cleaning.py                  # Further clean assessment titles
│   ├── final_cleaned_dataset.csv         # Final cleaned dataset (329 assessments)
│   ├── final_eda.py                      # EDA on cleaned dataset
│   ├── EDA.py                             # Additional EDA
│   ├── vectorized_model.py               # TF-IDF Vectorizer + Model training
│   ├── assessment_recommender_model.pkl  # Saved Nearest Neighbors model
│   ├── competency_vectorizer.pkl         # Saved TF-IDF vectorizer
│   ├── master.py                         # (Optional) Unified runner
│   ├── knowledge-graph.py                # Knowledge Graph (future work)
│   ├── training_ready_dataset.csv        # Dataset for model training
│   ├── cleaned_competency_dataset.csv    # Post-EDA cleaned data
│   └── README.md                         # 📄 This file
├── requirements.txt                                   # Python dependencies
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-link>
   cd SHL-Assess-Rec-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔄 End-to-End Workflow

### 1. Web Scraping

- Script: `shl-scraping.py`
- Scrape SHL assessment titles, descriptions, competencies.
- Save output to `shl_catalog.csv`.

### 2. Initial Cleaning

- Script: `after-scraping-cleaning.py`
- Clean basic text issues.
- Output: `cleaned_data.csv`

### 3. Deep Cleaning

- Script: `deep_cleaning.py`
- Remove titles with suspicious years or special characters.
- Final output: `final_cleaned_dataset.csv` (329 assessments).

### 4. Exploratory Data Analysis (EDA)

- Scripts: `EDA.py`, `final_eda.py`
- Analyze total assessments and unique competencies.
- 📊 Example:
  - Assessments: 329
  - Unique Competencies: 8
  - Most common: `Knowledge Of Subject`, `Problem Solving`, `Sales Skills`

### 5. Vectorization + Model Training

- Script: `vectorized_model.py`
- TF-IDF vectorization of competencies.
- Trained a **K-Nearest Neighbors** model for recommendations.
- Saved artifacts:
  - `competency_vectorizer.pkl`
  - `assessment_recommender_model.pkl`

### 6. Recommendation

- Given a competency input, recommend 5 closest matching assessments.
- Example output:
  ```
  Recommended Assessments:
  ['Entry Level Technical Support Solution', 'Universal Competency Framework Job Profiling Guide', 'Entry Level Sales Solution', 'Entry Level Hotel Front Desk Solution', 'Hipo Assessment Report 2.0']
  ```

---

## 📈 Current Status

- Cleaned dataset with 329 assessments.
- 8 unique competencies identified.
- Recommender system built and ready.

## 📝 Future Improvements

- Build a full **Knowledge Graph** using `knowledge-graph.py`.
- Add competency expansion using external datasets.
- Improve model performance metrics.

---

##Try it Out!
https://shl-assessment-recommendation-system-w9jhas2ka9healguutj68w.streamlit.app/

## 👨‍💻 Author

- Palak Aggarwal
- 2025, Graphic Era Hill University, Dehradun

---

Happy Learning! 🚀

