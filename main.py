from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3


main = Tk()
reader = Tk()

def sendData():
    titleContent = titleBox.get()
    location = placeBox.get()
    yearStr = yearBox.get()
    yearInt = int(yearStr)
    cursor.execute("INSERT INTO people (title, place, year) VALUES(?, ?, ?)", [titleContent, location, yearInt])
    cursor.execute("SELECT * FROM people")
    sendButton.config(state=DISABLED)

def readData() :
    global data
    global list1
    global listLength
    list1 = []
    listLength = len(list1)
    data = cursor.execute('''SELECT * FROM people''')
    for row in data:
        list1.append(row)
        listLength = len(list1)
    dataLabel = Label(reader, text=list1)

def closeConn() :
    connection.commit()
    connection.close()
    exit()


main.title("SQL Test")
reader.title("View")
connection = sqlite3.connect('people.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS people
             (title TEXT, place TEXT, year INT)''')
titleBox = Entry(main, width=30, borderwidth=10)
titleBox.grid(row=0, column=0)
placeBox = Entry(main, width=30, borderwidth=10)
placeBox.grid(row=1, column=0)
yearBox = Entry(main, width=30, borderwidth=10)
yearBox.grid(row=2, column=0)
sendButton = Button(main, text="Enter Data", padx=10, pady=10, bg="green", command=sendData)
closeButton = Button(main, text="Save And Close", padx=10, pady=10, bg="red", command=closeConn)
sendButton.grid(row=3, column=0)
sendButton.grid(row=4, column=0)
titleLabel = Label(main, text="Title").grid(row=0, column=1)
placeLabel = Label(main, text="Place").grid(row=1, column=1)
yearLabel = Label(main, text="Year").grid(row=2, column=1)
readButton = Button(reader, text="Read", padx=10, pady=10, bg="green", command=readData)
readButton.grid(row=0, column=0)
expLabel = Label(reader, text="Press to Read All Data").grid(row=0, column=1)

main.mainloop()
reader.mainloop()
