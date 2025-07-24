
# 🎬 Movie Recommender App

A simple content-based movie recommendation system built using **Streamlit** and **machine learning**. Select a movie you like, and it will recommend similar movies based on genre, keywords, cast, and more!

---

## 🚀 Features

- 🎞️ Recommend 5 similar movies based on the one you choose
- ⚡ Fast, interactive, and easy-to-use UI (Streamlit)
- 🧠 Uses `CountVectorizer` + `Cosine Similarity` for recommendations
- 📦 Preprocessed with TMDB 5000 Movie Dataset

---

## 🛠️ Tech Stack

- Python
- Pandas, Numpy
- Scikit-learn
- Streamlit

---

## 📁 Folder Structure

```

movie-recommender/
│
├── app.py                # Streamlit web app
├── model\_building.ipynb  # Jupyter notebook
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

> 📂 **Note:**  
> - The **dataset is not uploaded** due to file size limits. Please download it manually from the link below.  
> - The **`movies.pkl`** and **`similarity.pkl`** files are also not uploaded. They will be generated automatically when you run all cells in `model_building.ipynb`.

---

## 📦 Installation

1. Clone the repo

2. Install dependencies:

```bash
pip install -r requirements.txt
````

3. Run the app:

```bash
streamlit run app.py
```

---

## 📊 Dataset

* [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 👨‍💻 Author

Made with ❤️ by Aayush Pardeshi

```
