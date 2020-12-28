from flask import Flask, url_for, request, redirect, abort, jsonify
from BookDao import BookDao

app = Flask(__name__, static_url_path='', static_folder= 'staticpages')

@app.route('/')
def index():
    return "hello"

# get all
@app.route('/books')
def getAll():
    return jsonify(BookDao.getAll())

# find by id
@app.route('/books/<int:id>')
def findById(id):
    return jsonify(BookDao.findById(id))

# create
# curl -X POST -d "{"\title\":"\test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books 

@app.route('/books', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    book ={
        "id": request.json["id"],
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    return jsonify(BookDao.create(book))

    return "served by Create"

    # update 
    # curl -X PUT -d "{\"title\":\"test2\", \"price\":999}" -H Content-Type:application/json http://127.0.0.1:5000/books/123

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook=BookDao.findById(id)
    #print(foundBook)
    if  foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
        currentBook['price'] = request.json['price']
    BookDao.update(currentBook)

    return jsonify(currentBook)

# delete
# curl -X Delete http://127.0.0.1:5000/books/123

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    BookDao.delete(id)

    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)
