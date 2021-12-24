#!/usr/bin/env python # Allowing it to run
from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3

main = Tk()
main.minsize(410, 310)
readerBox = Frame(main, bg="light blue", height=100)

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
    global frame1
    frame1 = Frame(main)
    frame1.grid(row=5, column=1)
    global data
    global dataLabel
    global labelList
    labelList = []
    data = cursor.execute('''SELECT * FROM cars''')
    for row in data:
        dataLabel = Label(frame1, text=row)
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
    frame1.destroy()


main.title("Vulture DB")
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
sendButton = Button(main, text="Enter Data", padx=10, pady=10, bg="green", command=sendData).grid(row=3, column=0)
closeButton = Button(main, text="Save And Close", padx=10, pady=10, bg="red", command=closeConn).grid(row=3, column=1)
companyLabel = Label(main, text="Company").grid(row=0, column=0)
modelLabel = Label(main, text="Model").grid(row=1, column=0)
yearLabel = Label(main, text="Year").grid(row=2, column=0)
readButton = Button(readerBox, text="Read", padx=10, pady=10, bg="green", command=readData).pack()
clearButton = Button(readerBox, text="Clear Printed Lines", padx=10, pady=10, bg="grey", fg="grey", command=clearData, state=DISABLED)
clearButton.pack()
clearTableButton = Button(readerBox, text="Clear All Table Rows", padx=10, pady=10, bg="red", command=clearTable).pack()
credit = Label(readerBox, text="Made By Aadiraj Anil", bg="light blue")
credit.pack()


readerBox.grid(row=5, column=0)
main.mainloop()
