import pandas as pd
import streamlit as st
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


@st.cache_resource
def load_model():
    data_fake = pd.read_csv('Fake.csv')
    data_true = pd.read_csv('True.csv')

    data_fake["class"] = 0
    data_true["class"] = 1

    data = pd.concat([data_fake, data_true], axis=0)

    data = data.drop(['title', 'subject', 'date'], axis=1)

    data = data.sample(frac=1).reset_index(drop=True)


    data['text'] = data['text'].apply(wordopt)

    x = data['text']
    y = data['class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    vectorizer = TfidfVectorizer()
    xv_train = vectorizer.fit_transform(x_train)

    model = LogisticRegression()
    model.fit(xv_train, y_train)

    return model, vectorizer

model, vectorizer = load_model()

# PREDICTION FUNCTION
def predict_news(news):
    cleaned = wordopt(news)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)

    return "🟥 Fake News" if prediction[0] == 0 else "🟩 Real News"


#STREAMLIT
st.set_page_config(page_title="Factify", page_icon="📰")

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>📰 Factify</h1>
    <h4 style='text-align: center;'>Fake News Detection System</h4>
    """,
    unsafe_allow_html=True
)

st.write("---")

input_text = st.text_area("✍️ Enter News Article:")

if st.button("🔍 Check News"):
    if input_text.strip() == "":
        st.warning("Please enter some news text.")
    else:
        result = predict_news(input_text)
        st.success(f"Prediction: {result}")
        #In the terminal write "streamlit run app.py"
