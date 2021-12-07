from tkinter import *

master = Tk()
master.title("Project Vulture Test")
master.geometry("360x305")
# I use camelcase to code. I prefer it but I do know that Python's Official Formatting is PEP-8.
# Currently the Label is packed into the screen but it could be changed
testLabel = Label(master, text="Testing", font="Helvetica, 18").pack()


master.mainloop()