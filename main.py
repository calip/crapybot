from flask import Flask, json, request
import requests
from crapy import Crapy

# companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/')
def __init__():
  return 'CrapyBot'

# @api.route('/companies', methods=['GET'])
# def get_companies():
#   return request.args.get('user')
#   # return json.dumps(companies)

@api.route('/crap', methods=["POST"])
def postcrap():
  input_json = request.get_json(force=True)
  crapy = Crapy()
  datas = crapy.get_data(input_json['url'])
  return datas

if __name__ == '__main__':
  api.run()