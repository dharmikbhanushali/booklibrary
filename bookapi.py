from flask import Flask
from flask import request
import db


app = Flask(__name__)

@app.route('/')
def index():
	return "This is book api"

@app.route('/isbn/<isbnNumber>', methods = ['GET'])
def getBookByISBN(isbnNumber):
	return db.getBookByISBN(isbnNumber)

@app.route('/author/<author_name>', methods = ['GET'])
def getBookByAuthor(author_name):
	return db.getBookByAuthor(author_name)

@app.route('/addbook', methods = ['POST'] )
def addBook():
	print(request.json["bookdetails"])
	return db.addBook(request.json["isbn"], request.json["bookdetails"])

@app.route('/deletebook/<isbn_number>', methods = ['GET'] )
def deleteBookByISBN(isbn_number):
	return db.deleteBookByISBN(isbn_number)
	



if __name__ == '__main__':
	app.run(debug = True)


