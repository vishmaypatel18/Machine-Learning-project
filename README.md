# Simple Spam Detection Mini Project

A beginner-friendly Machine Learning mini project with a small web interface.

## Tech used
- Python
- Flask (web interface)
- pandas (read the CSV dataset)
- scikit-learn
- CountVectorizer (counts words in a message)
- Multinomial Naive Bayes (classifies the message)

## Run the project

1. Install Python 3.10 or newer.
2. Extract this folder and open a terminal inside it.
3. (Optional but recommended) Create a virtual environment:

   Windows:
   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```

4. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Open the local address shown in the terminal, usually:
   http://127.0.0.1:5000

## Try these messages
- `Congratulations you have won a free prize click now`
- `Hey, are we still meeting after class?`
- `Claim your cash reward now`

## How it works
1. `spam.csv` contains example messages labelled `spam` or `ham` (`ham` means not spam).
2. `CountVectorizer` turns the words into word-count numbers.
3. `MultinomialNB` learns patterns from the labelled examples.
4. When you submit a message, the model predicts `spam` or `ham`.
5. Flask shows the result in the browser.

## Important note
This project uses a small, hand-written example dataset so it is easy to understand and runs without downloading a dataset. It is for learning and demonstration, not reliable real-world spam filtering. A message marked “safe” is only the model's prediction; do not trust it for links, payments, or account security.
