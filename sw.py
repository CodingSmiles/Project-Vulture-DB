#!/usr/bin/env python 
from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3

main = Tk()
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
    global frame1
    frame1 = Frame(main)
    frame1.grid(row=7, column=1)
    global data
    global dataLabel
    global labelList
    labelList = []
    data = cursor.execute('''SELECT * FROM cars''')
    for row in data:
        dataLabel = Label(frame1, text=row)
        dataLabel.pack()
        labelList.append(dataLabel)
    clearButton.config(state=ACTIVE)


def closeConn() :
    connection.commit()
    connection.close()
    exit()


def clearData() :
    for dataLabel in labelList:
        dataLabel.destroy()
    frame1.destroy()
    clearButton.config(state=DISABLED, bg="red")


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
sendButton = Button(main, text="Enter Data", padx=10, pady=10, bg="green", command=sendData).grid(row=4, column=0)
closeButton = Button(main, text="Save And Close", padx=10, pady=10, bg="red", command=closeConn).grid(row=4, column=1)
companyLabel = Label(main, text="Company").grid(row=0, column=0)
modelLabel = Label(main, text="Model").grid(row=1, column=0)
yearLabel = Label(main, text="Year").grid(row=2, column=0)
readButton = Button(main, text="Read", padx=10, pady=10, bg="green", command=readData).grid(row=6, column=0)
clearButton = Button(main, text="Clear Printed Lines", padx=10, pady=10, bg="red", command=clearData)
clearButton.grid(row=7, column=0)
clearButton.config(state=DISABLED)
clearTableButton = Button(main, text="Clear All Table Rows", padx=10, pady=10, bg="red", command=clearTable).grid(row=8, column=0)
credit = Label(main, text="Made By Aadiraj Anil")
credit.grid(row=10, column=0)

main.mainloop()