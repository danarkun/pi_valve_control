from tkinter import *
from turtle import width

gui = Tk()
class Demo1:
    def __init__(self, master, label):
        self.statusBool = False
        self.master = master
        self.label = label
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = label)
        self.text.pack()

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=self.toggleStatus)
        self.button.pack()

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.pack()

        self.frame.pack()
    
    def toggleStatus(self):
        self.statusBool = not self.statusBool
        self.status.config(bg= "green" if self.statusBool else "red")
        print(self.statusBool)

app = Demo1(gui, "One")
gui.title("Valve Control")
# set window size
gui.geometry("480x320")

# f1 = Frame(gui)
# f1.pack()

# l1 = Label(f1, text = "First")
# l2 = Label(f1, text = "Second")
# l3 = Label(f1, text = "Third")

# l1.grid(row = 0, column = 0)
# l2.grid(row = 0, column = 1, padx = 160)
# l3.grid(row = 0, column = 2, padx = 0)

# entry widgets, used to take entry from user
# e1 = Entry(gui)
# e2 = Entry(gui)
  
# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)

gui.mainloop()