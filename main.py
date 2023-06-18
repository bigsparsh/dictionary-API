from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('dictionary.csv')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<word>")
def dictionary(word):
    definition = df['definition'].loc[df['word'] == word].squeeze()
    return {"word": str(word),
            "definition": definition}


app.run(debug=True)
