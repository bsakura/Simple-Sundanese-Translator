from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from translator import *

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/query',methods=['POST'])
@cross_origin()

def translating():
    datas = request.get_json()

    kata = datas['key']
    method = datas['algorithm']
    language = datas['bhs']

    print(kata, language, method)
    hasil = translate(kata, language, method)
    print("HASIL", hasil)

    return jsonify({'data' : hasil}),200
  