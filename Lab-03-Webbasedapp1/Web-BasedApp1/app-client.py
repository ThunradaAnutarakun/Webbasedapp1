from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#GET REST APIs
@app.route('/getuser/<idmemo>', methods=['GET'])
def getuser(idmemo):
    apiurl = 'http://localhost:5000/getuser/v1/' + idmemo
    response = requests.get(apiurl)
    return jsonify(response.json())

#POST REST APIs
@app.route('/postuser', methods=['GET'])
def postuser():
    data = {"firstname": "Pitchadanut", "lastname": "Promnoo", "email": "FairPP2004@gmail.com"}
    api_url = 'http://localhost:5000/postuser' 
    response = requests.post(api_url, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)