# m09_model_deployment.py
import joblib
import os
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.data.path.append('/home/ubuntu/nltk_data')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

clf = joblib.load(os.path.join(os.path.dirname(__file__), 'modelo.pkl'))
vect = joblib.load(os.path.join(os.path.dirname(__file__), 'vectorizer.pkl'))
mlb = joblib.load(os.path.join(os.path.dirname(__file__), 'generos.pkl'))

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_plot(plot):
    plot = plot.lower()
    plot = plot.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(plot)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t, pos='v') for t in tokens]
    return ' '.join(tokens)

def predict_genres(plot):
    clean_plot = preprocess_plot(plot)
    X = vect.transform([clean_plot])
    y_pred = clf.predict(X)
    genres = mlb.inverse_transform(y_pred)
    return list(genres[0]) if genres else ['Unknown']
