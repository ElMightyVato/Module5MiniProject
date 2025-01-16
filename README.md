Library Management System

Overview

This Library Management System is a Python-based application designed to manage books, users, and authors in a library. The application interacts with a MySQL database to store and retrieve data.

Features

Book Management

Add new books to the library.

Display all books along with all neccessary information.

User Management

Add new library users.

Display all confirmed users.

Author Management

Add new authors.

Display all authors along with their bios.

Project Structure

The project consists of three main files:

1. Class File (Classes.py)

This file defines the classes used in the application along with ways to work with the database.

Classes and Methods:

Book Class

add_book(title, author_id, isbn, publication_date): Adds a new book to the database.

display_books(): Displays all books and their details.

User Class

add_user(name, library_id): Adds a new user to the database.

display_users(): Displays all users and their information.

Author Class

add_author(name, biography): Adds a new author to the database.

display_authors(): Displays all authors and their information.

2. Database File (database.py)

This file establishes the connection to the MySQL database and provides the SQL schema for creating necessary tables.

Tables Created:

authors

books

users

borrowed_books

Database Connection:

The connect_database() function establishes the connection to the MySQL database using the following credentials:

Database Name: library_management

User: ************

Password: *************

Host: 127.0.0.1

Here is my database schema provided you don't have access to my current database:
CREATE DATABASE Library_Management;

USE Library_Management;

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    biography TEXT
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    isbn VARCHAR(30) NOT NULL UNIQUE,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    library_id VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

Lastly here are some examples utilzing this application:

Add a new book:

Select Book Operations > Add a new book.

Enter the book title, author ID, ISBN, and publication date.

Display all books:

Select Book Operations > Display all books.

View the list of all books along with their availability status.

Add a new user:

Select User Operations > Add a new user.

Enter the user's name and unique library ID.

Add a new author:

Select Author Operations > Add a new author.

Enter the author's name and biography.
