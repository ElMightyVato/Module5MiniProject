from database import connect_database

conn = connect_database() # using this from my database 

cursor = conn.cursor() # Easier access to excecute my queries

class Book:
    def __init__(self, title, author_id, isbn, publication_date): 
        self.title = title # This is for the book title
        self.author_id = author_id # The author
        self.isbn = isbn # The unique number used to track book
        self.publication_date = publication_date # When it came out

    def add_book(title, author_id, isbn, publication_date):
        query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)" # Created this query to add to my database for books by inserting the data into
        # title, author, isbn, and release date
        cursor.execute(query, (title, author_id, isbn, publication_date))
        conn.commit() # Pushing it to database by commiting
        print("Book added successfully!")

    def display_books():
        query = "SELECT books.id, books.title, authors.name, books.isbn, books.availability FROM books LEFT JOIN authors ON books.author_id = authors.id"
        # Using select to grab data from my books and authors table while also joining them on their primary and foreign keys
        cursor.execute(query)
        books = cursor.fetchall() # Here we are retrieving all darta in our rows.
        print("\nBooks in the Library:")
        print("ID | Title | Author | ISBN | Availability")
        for book in books: # Iterating our books 
            print(f"{book[0]} | {book[1]} | {book[2]} | {book[3]} | {'Available' if book[4] else 'Borrowed'}")

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_user(name, library_id):
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)" # Here we are adding the name and their unique library id so we can't have duplicate id's
        cursor.execute(query, (name, library_id))
        conn.commit()
        print("User added successfully!")
    
    def display_users():
        query = "SELECT id, name, library_id FROM users"
        cursor.execute(query)
        users = cursor.fetchall() # Gathering all data in our rows for users
        print("\nUsers in the Library:")
        print("ID | Name | Library ID")
        for user in users:
            print(f"{user[0]} | {user[1]} | {user[2]}")

class Author:
    def add_author(name, biography):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (name, biography))
        conn.commit()
        print("Author added successfully!")

    def display_authors():
        query = "SELECT id, name, biography FROM authors"
        cursor.execute(query)
        authors = cursor.fetchall()
        print("\nAuthors in the Library:")
        print("ID | Name | Biography")
        for author in authors:
            print(f"{author[0]} | {author[1]} | {author[2]}")

