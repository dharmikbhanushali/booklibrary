import requests
from flask import Flask


app = Flask(__name__)

@app.route('/')
def new():
	api_response = requests.post('http://127.0.0.1:5000/book', json = {'name': 'dharmik'})
	html_doc = "<html><body><b>" + api_response.json()['name'] + " " + api_response.json()['cost'] +  "</b></body></html>"
	return html_doc

#print(x.text)


if __name__ == '__main__':
	app.run(port = 5001, debug=True)