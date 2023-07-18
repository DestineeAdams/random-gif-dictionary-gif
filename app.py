from flask import Flask, render_template
import getData


app = Flask(__name__, template_folder='templates')


content = getData.getContent()


@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
   app.run(debug=True)