import mysql.connector
from mysql.connector import Error

# How I created my tables in mysql
"""CREATE DATABASE Library_Management;

USE Library_Management;

Create Table authors ( 
	id INT auto_increment primary key,
    name varchar(200) not null,
    biography text);

Create Table books (
	id INT Auto_increment Primary key,
    title varchar(200) not null,
    author_id int,
    isbn varchar(30) not null unique,
    publication_date Date,
    availability boolean default 1,
    foreign key (author_id) references authors(id)
    );

Create table users (
    id INT auto_increment primary key,
    name varchar(200) NOT NULL,
    library_id VARCHAR(20) not null unique);
    
CREATE TABLE borrowed_books (
    id INT auto_increment primary key,
    user_id INT,
    book_id INT,
    borrow_date DATE not null,
    return_date DATE,
    foreign key (user_id) references users(id),
    foreign key (book_id) references books(id)
    ); """

# Establishing my connection
def connect_database():
    """ Connect to the MYSQL database and return the connection object"""
    # Database connection parameters
    db_name = "library_management"
    user = "ElMightyVato"
    password = "NeroZero1377@"
    host = "127.0.0.1"

    try: 
    # Attempting to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

    # Check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
    # Handling any connection errors
        print(f"Error: {e}")
        return None  