from flask import Flask, render_template
import getAPIData as gad



app = Flask(__name__)

if __name__ == '__app__':
    app.run(debug=True)




@app.route('/')
def index():
    content = gad.getData()
    
    return render_template("index.html", term = content["term"], defintion = content["defintion"], gif = str(content["gif"]))

