# sql.py - Creating a SQLite3 table and populate it with data

import sqlite3

# creating a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as conn:

    # getting a cursor object used to execute SQL commands
    c = conn.cursor()

    # creating the table
    c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    # inserting dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    
