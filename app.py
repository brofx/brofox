from flask import Flask, render_template
from random import choice

app = Flask(__name__)


backgrounds = [
"ark.jpg",
"rl.jpg",
"csgo.jpg",
"dota2.jpg"
]

@app.route("/")
def index():
    return render_template("index.html", bg=choice(backgrounds))

if __name__ == "__main__":
    app.run(debug=True, port=8001, host="0.0.0.0")
