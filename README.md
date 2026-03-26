Factify – The Fake News Detector

Project Overview
In today’s digital world, we see news everywhere — social media posts, forwarded messages, and online articles. The problem is that a lot of this information is misleading or completely fake, and it’s becoming harder to tell what’s real.
Factify is a simple web application that helps solve this problem. It allows users to paste any news content and quickly check whether it is likely real or fake using a machine learning model.

Here are some Features that makes Factify relevant and Important -
1. Simple and easy-to-use interface
2. Instant prediction
3. Works with any text-based news
4. Fast and lightweight

How It Works - 
First, the input text is cleaned by converting it to lowercase and removing unnecessary characters.
Then, TF-IDF is used to convert the text into numerical form by identifying important words.
Finally, a Logistic Regression model predicts whether the news is Real or Fake based on patterns learned from the dataset.

Tech Stack - Python
             Pandas
             Scikit-learn
             Streamlit

Project Structure
app.py – Main application file
Fake.csv – Fake news dataset
True.csv – Real news dataset

Setup Instructions

1. Install Python on your system and make sure it is added to PATH
2. Install required libraries using:
3. pip install pandas scikit-learn streamlit
4. Place Fake.csv and True.csv in the same folder as app.py
5. Run the app using: streamlit run app.py
6. After running, a browser window will open where you can interact with the app.

Usage - 
Copy any news article or message
Paste it into the input box
Click the check button
The app will show whether the news is Real or Fake

Future Improvements - 
1. To Improve the UI design
2. Use more advanced machine learning models
3. Deploy the app online
4. Add confidence scores for predictions

Final Note - 
Factify is a simple project built to address the growing problem of fake news. It shows how machine learning can be used in a practical way to help people make better decisions about the information they consume.

Screenshots of News Authentications - 
1. Real News Authentication
<img width="1919" height="1016" alt="Screenshot 2026-03-27 000016" src="https://github.com/user-attachments/assets/8b70cb34-1cb2-42aa-b526-ca9d97b46359" />
2. Fake News Authentication
   <img width="1919" height="1023" alt="Screenshot 2026-03-27 000058" src="https://github.com/user-attachments/assets/4729cfbe-272a-4fe6-ad53-494acf2dce63" />
