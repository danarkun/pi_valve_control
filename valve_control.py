from tkinter import *
from turtle import width
# import RPi.GPIO as GPIO

GPIO_1 = 20
GPIO_2 = 21
GPIO_3 = 26

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(GPIO_1, GPIO.OUT)
# GPIO.setup(GPIO_2, GPIO.OUT)
# GPIO.setup(GPIO_3, GPIO.OUT)

class MainApp(Frame):
    def __init__(self, master):
        self.master = master
        self.ctl1 = Frame(self.master)
        self.ctl2 = Frame(self.master)
        self.ctl3 = Frame(self.master)
        self.frame4 = Frame(self.master)

        self.pwr = PowerPanel(self.frame4)
        self.frame4.grid(row=0, column=1)

        self.cp1 = ControlPanel(self.ctl1, GPIO_1)
        self.ctl1.grid(row=1, column=0)

        self.cp2 = ControlPanel(self.ctl2, GPIO_2)
        self.ctl2.grid(row=1, column=1)

        self.cp3 = ControlPanel(self.ctl3, GPIO_3)
        self.ctl3.grid(row=1, column=2)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)

class PowerPanel:
    def __init__(self, master):
        self.statusBool = False
        self.master = master
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = "Pump Power")
        self.text.grid(row=0, column=0)

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=self.toggleStatus)
        self.button.grid(row=1, column=0)

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.grid(row=2, column=0)

        self.frame.pack()

    def toggleStatus(self):
        self.statusBool = not self.statusBool
        self.status.config(bg= "green" if self.statusBool else "red")
        # GPIO.output(self.gpio, self.statusBool)
        print(f'GPIO{self.gpio} is: {self.statusBool}')

class ControlPanel:
    def __init__(self, master, gpio):
        self.statusBool = False
        self.master = master
        self.label = gpio
        self.gpio = gpio
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = gpio)
        self.text.grid(row=0, column=0)

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=self.toggleStatus)
        self.button.grid(row=1, column=0)

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.grid(row=2, column=0)

        self.frame.pack()
    
    def toggleStatus(self):
        self.statusBool = not self.statusBool
        self.status.config(bg= "green" if self.statusBool else "red")
        # GPIO.output(self.gpio, self.statusBool)
        print(f'GPIO{self.gpio} is: {self.statusBool}')

def main():
    gui = Tk()
    app = MainApp(gui)
    gui.title("Valve Control")
    # set window size
    gui.geometry("480x320")
    gui.mainloop()

if __name__ == "__main__":
    main()