"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    hist = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    return hist

@app.route("/")
def home():
  hist_returned = before_first_request()
  word = hist_returned.sample()
  return f"Here's a random word: {word}"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
