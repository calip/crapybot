from app import app
from flask import json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

@app.route('/')
@app.route('/index')
def index():
    return 'CrapyBot'

@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)