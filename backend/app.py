from flask import Flask
import getAPIData as gad
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder='./front/build', static_url_path='')
cors = CORS(app)




@app.route('/words', methods=['GET'])
@cross_origin()
def words():
    content = gad.getData()
    return content

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run()
