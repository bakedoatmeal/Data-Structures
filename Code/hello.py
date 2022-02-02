from flask import Flask
from histogram import histogram_dict
from sampling import getWeightedWord

app = Flask(__name__)

@app.route("/")
def hello_world():
  hist = histogram_dict('sampletext.txt')
  word = getWeightedWord(hist)
  return f"Here's a random word from Sherlock Holmes: {word}"