from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
	return {
		"message": "Padharo mare des"
	}

@app.route('/name')
def give_name():
	return "My name is practise"

# Function returns book
@app.route('/book', methods = ['POST'])
def book_details():
	print(request.json)
	return {
	"name": request.json['name'],
	"cost":"500"

	}


if __name__ == '__main__':
	app.run(debug = True)