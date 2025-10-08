# Netflix Reviews Sentiment Analysis

Analyze customer reviews from Netflix using Natural Language Processing (NLP) to classify feedback into **Positive**, **Neutral**, or **Negative** sentiments.  
This project helps visualize audience perceptions, uncover trends, and support data-driven decisions through an interactive **Streamlit web app**.


### Features
- **Data Collection** — Scrape Netflix reviews from Play Store & App Store  
- **Data Cleaning & Preprocessing** — Remove noise, clean text, handle duplicates  
- **Sentiment Analysis** — Classify reviews into 3 categories:  
  - Positive  
  - Neutral  
  - Negative  
- **Visualizations** — WordClouds, bar charts, sentiment trends  
- **Streamlit Dashboard** — Interactive interface for exploring insights  
- **Automation Scripts** — For fast, repeatable analysis


### Sentiment Categories

| Category  | Description |
|-----------|-------------|
| 👍 Positive | Indicates satisfaction, praise, or enthusiasm |
| 😐 Neutral | Balanced, factual, or non-emotional feedback |
| 👎 Negative | Expresses dissatisfaction, complaints, or frustration |


### Tech Stack

- **Python** — Core programming language  
- **Streamlit** — Interactive web app  
- **Pandas** — Data manipulation & analysis  
- **Scikit-learn** — Sentiment model training & evaluation  
- **NLTK** — Text preprocessing & tokenization
- **VADER Sentiment** — Rule-based sentiment scoring
- **Matplotlib & Seaborn** — Data visualization & charts
- **WordCloud** — Visualizing frequent keywords in reviews
- **Imbalanced-learn (SMOTE)** — Handling class imbalance during training
- **Google Play Scraper** — Collecting Netflix app reviews from Play Store
- **Requests** — Web requests & API handling
- **Joblib** — Saving and loading ML models efficiently
- **Jupyter Notebooks** — Prototyping & experimentation


### Project Structure

```bash

netflix-sentiment-analysis/
├── assets/                     # Images, icons, or other static files
├── automation/                 # Scripts and pipelines for automated tasks
├── data/                       # Datasets (raw and processed reviews)
├── models/                     # Trained ML models and serialized files
├── notebooks/                  # Jupyter notebooks for exploration & training
├── scripts/                    # Python scripts for scraping, cleaning, and modeling
├── .gitignore                  # Git ignore file
├── app.py                      # Streamlit web application
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
```




