from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<word>")
def dictionary(word):
    df = pd.read_csv('dictionary.csv')
    definition = df['definition'].loc[df['word'] == word].squeeze()
    return {"word": str(word),
            "definition": definition}


app.run(debug=True)
