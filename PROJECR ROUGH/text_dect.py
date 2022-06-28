import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
user = st.text_input("Enter Text",key="t1")
data = pd.read_csv("dataset.csv")
print(data.head())
x = np.array(data["Text"])
y = np.array(data["language"])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.33,random_state=42)
model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)
user = st.text_input("Enter Text",key="t2")
if(st.button("Detect")):
	data = cv.transform([user]).toarray()
	output = model.predict(data)
	st.write(output)
