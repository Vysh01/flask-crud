from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = {
    1: {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'},
    2: {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
}

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return books


# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book

    return {'error':'Book not found'}

# Create a book
@app.route('/books', methods=['POST'])
def create_book():
    new_book={'id':len(books)+1, 'title':request.json['title'], 'author':request.json['author']}
    books.append(new_book)
    return new_book


# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book 
    return {'error':'Book not found'}

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"data":"Book Deleted Successfully"}

    return {'error':'Book not found'}


@app.route('/uploadbook', methods=['POST'])
def uploadbook():
    import os
    uploaded_file = request.files['file']
    if uploaded_file and allowed_file(uploaded_file.filename):
        destination = os.path.join('uploads/',uploaded_file.filename)
        uploaded_file.save(destination)
        return {'data':'File Uploaded Successfully'}

    else:
        return {'error':'File upload failed, or invalid file type'}


def allowed_file(filename):
    ALLOWED_EXTS = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS

# Run the flask App
if __name__ == '__main__':
    app.run(debug=True)