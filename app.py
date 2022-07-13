from flask import Flask, render_template, url_for
import getAPIData as gad
import os

app = Flask(__name__)

if __name__ == '__app__':
    app.run(debug=False)




@app.route('/')
def index():
    content = gad.getData()
    return render_template("index.html", term = content["term"], defintion = content["defintion"], gif = str(content["gif"]))
    # return render_template("index.html", term = "tying", defintion = " the act of tying or binding things together ", gif = "https://giphy.com/gifs/poseonfx-kb9LpghGziivyHPKUH")

