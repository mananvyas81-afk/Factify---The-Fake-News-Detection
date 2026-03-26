Factify – The Fake News Detector

Project Overview - 
This project is a simple web-based application built using Python and Streamlit. The main idea behind this project is to deal with the growing problem of fake news
that we see every day on social media, WhatsApp forwards, and different websites. Many times, people believe or share news without checking if it’s true or not.
So, I built Factify as a small solution to this problem. It allows users to enter any news content and quickly check whether it is real or fake using a machine 
learning model. The focus of this project was to keep it simple, fast, and easy to use for anyone.

Key Functionality
• Takes news text as input from the user
• Cleans and processes the text before analysis
• Uses TF-IDF to convert text into numerical form
• Applies a Logistic Regression model for prediction
• Displays the result (Real or Fake) instantly
• Provides a simple and interactive user interface

Features
• Easy-to-use interface where users can directly paste text
• Quick prediction without long waiting time
• Lightweight model that runs smoothly
• Clean and simple design without unnecessary complexity
• Works entirely on text input

Technologies & Tools Used - 
Category Tool / Library - 1.Language - Python 3.x
                          2.Framework - Streamlit
                          3.Libraries - Pandas, Scikit-learn
                          4.ML Techniques - TF-IDF, Logistic Regression


Steps to Run the Project
•Prerequisites - 
You just need Python 3.x installed on your system. No extra setup is required.

Setup -
1. Save the code in a file named app.py
2. Make sure Fake.csv and True.csv are in the same folder
3.Open terminal or command prompt, go to the project folder, and run:
streamlit run app.py
4.After this, the app will automatically open in your browser.
5.Run the application using the command above
6.Enter News Content(Paste any news article or message into the input box)
7.Check Result - 
• Click the button to analyze the news
• The app will show whether it is Real or Fake
8.Try Different Inputs
• You can test multiple examples to see how the model behaves
9.Output
• The result appears instantly on the screen
