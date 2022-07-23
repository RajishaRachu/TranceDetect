from PIL import Image
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Users\Evin Jith\AppData\Local\Programs\Tesseract-OCR\tesseract"
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
li='tam+hin+eng+fra+chi_sim+mal+ara'
img='mal2.png'
def canny(image):
    return cv2.Canny(image, 100, 200)

lan_li={'[\'French\']':'fra','[\'Tamil\']':'tam','[\'English\']':'eng','[\'Hindi\']':'hin','[\'Chinese\']':'chi_sim','[\'Arabic\']':'ara'}
text=tess.image_to_string(Image.open(img),lang=li)
print(text)
data = pd.read_csv("dataset.csv")
x = np.array(data["Text"])
y = np.array(data["language"])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.33,random_state=42)
model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)
data = cv.transform([text]).toarray()
output = model.predict(data)
print(output)
output=str(output)
r_output=lan_li[output]
print(r_output)
text=tess.image_to_string(Image.open(img),lang=r_output)
print(text)
data = pd.read_csv("dataset.csv")
x = np.array(data["Text"])
y = np.array(data["language"])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.33,random_state=42)
model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)
data = cv.transform([text]).toarray()
output = model.predict(data)
print(output)