#!/usr/bin/env python # Allowing it to run
from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3

main = Tk()
reader = Tk()
reader.minsize(220, 125)
main.resizable(False, False)

def clearTable() :
    cursor.execute('DELETE FROM cars;',);
    for dataLabel in labelList:
        dataLabel.destroy()


def sendData():
    company = (companyBox.get())
    model = (modelBox.get())
    year = (yearBox.get())
    cursor.execute("INSERT INTO cars (company, model, year) VALUES(?, ?, ?)", [company, model, year])
    companyBox.delete(0, END)
    modelBox.delete(0, END)
    yearBox.delete(0, END)


def readData() :
    global data
    global dataLabel
    global labelList
    labelList = []
    data = cursor.execute('''SELECT * FROM cars''')
    for row in data:
        dataLabel = Label(reader, text=row)
        dataLabel.pack()
        labelList.append(dataLabel)
    clearButton.config(state=ACTIVE, bg="red", fg="black")


def closeConn() :
    connection.commit()
    connection.close()
    exit()


def clearData() :
    for dataLabel in labelList:
        dataLabel.destroy()
    clearButton.config(state=DISABLED, bg="grey", fg="grey")


main.title("Vulture DB")
reader.title("Reader")
connection = sqlite3.connect('cars.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS cars
             (company TEXT, model TEXT, year INT)''')
companyBox = Entry(main, width=30, borderwidth=10)
companyBox.grid(row=0, column=1)

modelBox = Entry(main, width=30, borderwidth=10)
modelBox.grid(row=1, column=1)
yearBox = Entry(main, width=30, borderwidth=10)
yearBox.grid(row=2, column=1)
sendButton = Button(main, text="Enter Data", padx=10, pady=10, bg="green", command=sendData).grid(row=4, column=0)
closeButton = Button(main, text="Save And Close", padx=10, pady=10, bg="red", command=closeConn)
closeButton.grid(row=4, column=1)
companyLabel = Label(main, text="Company").grid(row=0, column=0)
modelLabel = Label(main, text="Model").grid(row=1, column=0)
yearLabel = Label(main, text="Year").grid(row=2, column=0)
readButton = Button(reader, text="Read", padx=10, pady=10, bg="green", command=readData)
readButton.pack()
clearButton = Button(reader, text="Clear Printed Lines", padx=10, pady=10, bg="grey", fg="grey", command=clearData, state=DISABLED)
clearButton.pack()
clearTableButton = Button(reader, text="Clear All Table Rows", padx=10, pady=10, bg="red", command=clearTable).pack()
credit = Label(main, text="Made By Aadiraj Anil").grid(row=5, column=0)


main.mainloop()
reader.mainloop()
