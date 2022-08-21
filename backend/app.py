from contextlib import nullcontext
from flask import Flask, render_template, url_for
import getAPIData as gad
import os, json

app = Flask(__name__)

if __name__ == '__app__':
    app.run(debug=False)





@app.route('/words')
def words():
    content = gad.getData()

    # return json.dumps(content)
    return content