from flask import Flask, render_template, request, jsonify
from models import db, User, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_library.db'
db.init_app(app)


# User routes
@app.route('/api/users', methods=['POST'])
def create_user():
  data = request.get_json()

  new_user = User()
  new_user.username = data['username']
  new_user.password = data['password']
  new_user.email = data['email']

  db.session.add(new_user)
  db.session.commit()

  return jsonify({
      'opreation_type': "Created",
      'message': 'User created successfully',
      "user": {
          'id': new_user.id,
          'username': new_user.username,
          'email': new_user.email
      }
  })


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
  user = User.query.get(user_id)
  if user:
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })
  else:
    return jsonify({'message': 'User not found'})


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
  user = User.query.get(user_id)
  if user:
    data = request.get_json()
    user.username = data['username']
    user.password = data['password']
    user.email = data['email']
    db.session.commit()
    return jsonify({
        'opreation_type': "Updated",
        'message': 'User updated successfully',
        "user": {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })
  else:
    return jsonify({'message': 'User not found'})


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  user = User.query.get(user_id)
  if user:
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        'opreation_type': "Deleted",
        'message': 'User deleted successfully',
        "user": {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })
  else:
    return jsonify({'message': 'User not found'})


# Book routes
@app.route('/api/books', methods=['POST'])
def create_book():
  data = request.get_json()
  new_book = Book()
  new_book.title = data['title']
  new_book.author = data['author']
  new_book.genre = data['genre']
  new_book.language = data['language']
  new_book.cover_image = data['cover_image']
  new_book.user_id = data['user_id']

  db.session.add(new_book)
  db.session.commit()
  return jsonify({
      'opreation_type': "Created",
      'message': 'Book created successfully',
      "book": {
          'id': new_book.id,
          'title': new_book.title,
          'author': new_book.author,
          'genre': new_book.genre,
          'language': new_book.language,
          'cover_image': new_book.cover_image,
          'user_id': new_book.user_id
      }
  })


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
  book = Book.query.get(book_id)
  if book:
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'language': book.language,
        'cover_image': book.cover_image,
        'user_id': book.user_id
    })
  else:
    return jsonify({'message': 'Book not found'})


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  book = Book.query.get(book_id)
  if book:
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    book.genre = data['genre']
    book.language = data['language']
    book.cover_image = data['cover_image']
    book.user_id = data['user_id']
    db.session.commit()
    return jsonify({
        'opreation_type': "Updated",
        'message': 'Book updated successfully',
        'book': {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'language': book.language,
            'cover_image': book.cover_image,
            'user_id': book.user_id
        }
    })
  else:
    return jsonify({'message': 'Book not found'})


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
  book = Book.query.get(book_id)
  if book:
    db.session.delete(book)
    db.session.commit()
    return jsonify({
        'opreation_type': "Deleted",
        'message': 'Book deleted successfully',
        'book': {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'language': book.language,
            'cover_image': book.cover_image,
            'user_id': book.user_id
        }
    })
  else:
    return jsonify({'message': 'Book not found'})


@app.route('/')
def home_page():

  # new_book = Book()
  # new_book.title = 'Python Programming and SQL'
  # new_book.author = 'Mark Reed'
  # new_book.genre = 'Programming'
  # new_book.language = 'English'
  # new_book.cover_image = '61jXSsH1M8L._SL1430_.jpg'
  # new_book.user_id = 2

  # db.session.add(new_book)
  # db.session.commit()
  # return jsonify({'message': 'Book created successfully', 'book': new_book.title})

  # new_user = User()
  # new_user.username = "qkahmadzai1"
  # new_user.password = "kasdjs1d@332"
  # new_user.email = "qkahmadzai1@gmail.com"

  # db.session.add(new_user)
  # db.session.commit()
  # return jsonify({'message': 'User created successfully'})

  return render_template('home.html')


if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(host='0.0.0.0', debug=True)
