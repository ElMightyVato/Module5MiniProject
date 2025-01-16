from Classes import Book
from Classes import User
from Classes import Author
from database import connect_database

conn = connect_database()

cursor = conn.cursor()

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            isbn = input("Enter ISBN: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            Book.add_book(title, author_id, isbn, publication_date)
        elif choice == '2':
            Book.display_books()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. Display all users")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            User.add_user(name, library_id)
        elif choice == '2':
            User.display_users()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. Display all authors")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            Author.add_author(name, biography)
        elif choice == '2':
            Author.display_authors()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()