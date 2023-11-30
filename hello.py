# import requests
# response = requests.get('https://oxylabs.io/')
# print(response.text)

from flask import Flask, json, request
import requests

# companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/')
def init_root():
  return 'CrapyBot'

# @api.route('/companies', methods=['GET'])
# def get_companies():
#   return request.args.get('user')
#   # return json.dumps(companies)

@api.route('/crap', methods=["POST"])
def postcrap():
  input_json = request.get_json(force=True)
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
  response = requests.get(input_json['url'], headers=headers)
  # response = requests.get(input_json['url'])
  return json.dumps(response.text)

if __name__ == '__main__':
  api.run()