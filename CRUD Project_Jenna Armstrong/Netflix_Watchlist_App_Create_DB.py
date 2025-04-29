#This program will create a database for the GUI

#Import required libraries

from tkinter import *
from PIL import ImageTk, Image
import os, sys

import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Watchlist_Master
            (Date date,
            Title TEXT PRIMARY KEY,
            Category text,
            Genre text,
            Rating integer,
            Recommend text)''')
        self.conn.commit()

    #define function to return whole table
    def fetch(self):
        self.cur.execute("SELECT * FROM Watchlist_Master")
        rows = self.cur.fetchall()
        return rows

    #define function to add new entry to table
    def insert(self, Date, Title, Category, Genre, Rating, Recommend):
        self.cur.execute("INSERT OR REPLACE INTO Watchlist_Master VALUES (?,?,?,?,?,?)",
                        (Date, Title, Category, Genre, Rating, Recommend))
        self.conn.commit()

    #define function to update an entry
    def update(self, Date, Title, Category, Genre, Rating, Recommend):
        self.cur.execute('''UPDATE Watchlist_Master SET
                        Date=?, Category=?, Genre=?, Rating=?, 
                        Recommend=? WHERE Title=?''',
                        (Date, Category, Genre, Rating, Recommend, Title))
        self.conn.commit()

    #define function to remove an entry
    def remove(self, Title):
        self.cur.execute("DELETE FROM Watchlist_Master WHERE Title=?", (Title,))
        self.conn.commit()

    #define function to search Title
    def search_Title(self, Title):
        self.cur.execute("SELECT * FROM Watchlist_Master WHERE Title=?", (Title,))
        rows = self.cur.fetchall()
        return rows
    
    # define function to close
    def __del__(self):
        self.conn.close()


#path="C:\\Users\\jenna\\Documents\\Mt SAC\\CISP 71\\CRUD Project_Jenna Armstrong\\"
#db= Database(path +'Watchlist.db')

#db.insert(20160715, 'Stranger Things', 'TV Show', 'Sci-Fy', 4, 'Yes')
#db.insert(20210223, 'The Last Letter from Your Lover', 'Movie', 'Romance', 5, 'Yes')
#db.insert(20200131, 'Miss Americana', 'Documentary', 'Music', 5, 'Yes')
#db.insert(2020427, 'Never Have I Ever', 'TV Show', 'Comedy', 4, 'Yes')
#db.insert(20180511, 'The Kissing Booth', 'Movie', 'Rom-com', 1, 'No')


