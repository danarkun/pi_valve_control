from tkinter import *
from turtle import width

class MainApp(Frame):
    def __init__(self, master):
        self.master = master
        self.frame1 = Frame(self.master)
        self.frame2 = Frame(self.master)
        self.frame3 = Frame(self.master)

        self.cp1 = ControlPanel(self.frame1, "One")
        self.frame1.grid(row=0, column=0, padx=20)

        self.cp2 = ControlPanel(self.frame2, "Two")
        self.frame2.grid(row=0, column=1, padx=80)

        self.cp3 = ControlPanel(self.frame3, "Three")
        self.frame3.grid(row=0, column=2, padx=20)

class ControlPanel:
    def __init__(self, master, label, gpio):
        self.statusBool = False
        self.master = master
        self.label = label
        self.gpio = gpio
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = label)
        self.text.grid(row=0, column=0, pady=10)

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=self.toggleStatus)
        self.button.grid(row=1, column=0, pady=10)

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.grid(row=2, column=0, pady=20)

        self.frame.pack()
    
    def toggleStatus(self):
        self.statusBool = not self.statusBool
        self.status.config(bg= "green" if self.statusBool else "red")
        # GPIO.output(self.gpio, self.statusBool)
        print(self.statusBool)

def main():
    gui = Tk()
    app = MainApp(gui)
    gui.title("Valve Control")
    # set window size
    gui.geometry("480x320")
    gui.mainloop()

if __name__ == "__main__":
    main()