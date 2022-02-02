"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram_dict
from sampling import getWeightedWord

app = Flask(__name__)
hist = {}

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    hist = histogram_dict('sampletext.txt')

@app.route("/")
def home():
  word = getWeightedWord(hist)
  return f"Here's a random word from Sherlock Holmes: {word}"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
