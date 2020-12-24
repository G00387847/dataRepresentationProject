from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder= 'staticpages')

@app.route('/')
def index():
    return "hello"

# get all
@app.route('/books')
def getAll():
    return jsonify([])

# find by id
@app.route('/books/<int:ISBN>')
def findById(ISBN):
    return jsonify({})

# create
# curl -X POST -d "{"\title\":"\test\", \"author\":\"Handsome\",\"price\":123}" http://127.0.0.1:5000/books 

@app.route('/books', methods = ['POST'])
def create():
    if not request.json:
        abort(400)

    book ={
        "ISBN": request.json["ISBN"],
        "title": request.json["title"],
        "author": request.json["title"],
        "price": request.json["price"]
    }
    return jsonify({})

    return "served by Create"

@app.route('/books/<int:ISBN>', methods=['PUT'])
def update(id):
    foundBooks = []
    if len(foundBooks) == 0:
          return json({}), 404
    currentBook = foundBooks[0]
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
        currentBook['price'] = request.json['price']

    return jsonify(currentBook)

@app.route('/books/<int:ISBN>', methods=['DELETE'])
def delete(id):

    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)
