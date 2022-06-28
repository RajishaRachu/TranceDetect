import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

filePath = 'sample.pdf'
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

for page_number, page_data in enumerate(doc):
    txt = pytesseract.image_to_string(page_data)
    print("{}".format(txt))

data = pd.read_csv("dataset.csv")
x = np.array(data["Text"])
y = np.array(data["language"])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.33,random_state=42)
model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)
data = cv.transform([txt]).toarray()
output = model.predict(data)
print(output)
