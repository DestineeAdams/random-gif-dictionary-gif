from flask import Flask
import getAPIData as gad


app = Flask(__name__, static_folder='../front/build', static_url_path='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))


@app.route('/words', methods=['GET'])
def words():
    content = gad.getData()
    return content

