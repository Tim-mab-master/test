from flask import Flask, jsonify, request 
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!!!!")

@app.route('/shoplist', methods=['GET'])
def shoplist():
    return("Buy Buy!!!!")


if __name__ == "__main__":
    app.run(debug=True)
