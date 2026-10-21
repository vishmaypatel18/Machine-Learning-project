from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Load the small example dataset included with this project.
data = pd.read_csv("spam.csv")
data["label"] = data["label"].str.lower().str.strip()
data = data.dropna(subset=["message", "label"])

# Convert messages into word counts, then train a Naive Bayes classifier.
model = Pipeline([
    ("words", CountVectorizer()),
    ("classifier", MultinomialNB())
])
model.fit(data["message"], data["label"])

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    result = None
    confidence = None

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if message:
            prediction = model.predict([message])[0]
            probabilities = model.predict_proba([message])[0]
            confidence = round(float(max(probabilities)) * 100, 1)
            result = "spam" if prediction == "spam" else "safe"

    return render_template(
        "index.html",
        message=message,
        result=result,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
