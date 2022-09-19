from pickle import NONE
from flask import Flask, send_from_directory
import getAPIData as gad
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder='./front/build', static_url_path='/')
cors = CORS(app)




@app.route('/words', methods=['GET'])
@cross_origin()
def words():
    content = gad.getData()
    # testJson = {
    #     "backupterm": None ,
    #     "defintion":"the act of killing (an animal or person) in order to propitiate a deity",
    #     "gif":"https://giphy.com/embed/5wWf7GKTWtUS6uvkf2U",
    #     "term":"sacrifice"
    # }
    # return testJson
    return content

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, './index.html')


if __name__ == "__main__":
    app.run()
