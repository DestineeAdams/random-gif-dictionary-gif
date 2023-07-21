from flask import Flask, render_template
import getData


app = Flask(__name__, template_folder='templates')




@app.route('/')
def index(word=None, definition=None, gifURL=None):

    content = getData.getContent()
    print(content)
    
    return render_template('index.html', word=content["word"], definition=content["definition"], gifURL=content["gifURL"])
 
 


if __name__ == '__main__':
   app.run(debug=True)