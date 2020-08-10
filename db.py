import json
with open("book.json") as new:
	data = json.load(new)
	new.close()


def getBookByISBN(isbn):
	if isbn in data:
		return data[isbn]
	
	return {}

def getBookByAuthor(author_name):
	book_list = []
	for isbn in data:
		if data[isbn]['author'] == author_name:
			book_list.append(data[isbn]['name'])
			print(data[isbn]['author'])
	return {
		"book_list":book_list
	}

	return {}


def addBook(isbn, bookdetails):
	data[isbn] = bookdetails
	with open("book.json", "w") as libraryDb:
		json.dump(data, libraryDb,indent = 4, sort_keys = True)
		libraryDb.close()
	return {
		"message": "book added successfully"
	}
	

def deleteBookByISBN(isbn_number):
	if isbn_number in data:
		
			print(data[isbn_number])
			book_name = data[isbn_number]['name']
			book_author = data[isbn_number]['author']
			del data[isbn_number]
			with open("book.json","w") as updatedDb:
				json.dump(data, updatedDb,indent = 4, sort_keys = True)
				updatedDb.close()
				
			#print(data[isbn])
	return {
	"deleted_book": book_name,
	"book_author": book_author
	}