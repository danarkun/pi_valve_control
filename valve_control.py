from tkinter import *
from turtle import width
# import RPi.GPIO as GPIO

GPIO_VALVE1 = 20
GPIO_VALVE2 = 21
GPIO_VALVE3 = 26
GPIO_PWR = 18

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(GPIO_1, GPIO.OUT)
# GPIO.setup(GPIO_2, GPIO.OUT)
# GPIO.setup(GPIO_3, GPIO.OUT)
# GPIO.setup(GPIO_PWR, GPIO.OUT)

class MainApp(Frame):
    def __init__(self, master):
        self.master = master
        ctl1Frame = Frame(self.master)
        ctl2Frame = Frame(self.master)
        ctl3Frame = Frame(self.master)
        pwrFrame = Frame(self.master)

        cp1 = ControlPanel(ctl1Frame, GPIO_VALVE1)
        ctl1Frame.grid(row=1, column=0)

        cp2 = ControlPanel(ctl2Frame, GPIO_VALVE2)
        ctl2Frame.grid(row=1, column=1)

        cp3 = ControlPanel(ctl3Frame, GPIO_VALVE3)
        ctl3Frame.grid(row=1, column=2)

        pwr = PowerPanel(pwrFrame, [cp1, cp2, cp3], GPIO_PWR)
        pwrFrame.grid(row=0, column=1, pady=20)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)

class PowerPanel:
    def __init__(self, master, controlPanels, gpio):
        self.gpio = gpio
        self.controlPanels = controlPanels
        self.statusBool = False
        self.master = master
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = "Pump Power")
        self.text.grid(row=0, column=0, pady=10)

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=self.toggleStatus)
        self.button.grid(row=1, column=0, pady=10)

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.grid(row=2, column=0, pady=10)

        self.frame.pack()

    def toggleStatus(self):
        self.statusBool = not self.statusBool
        self.status.config(bg= "green" if self.statusBool else "red")
        # GPIO.output(self.gpio, self.statusBool)
        print(f'Power is: {self.statusBool}')

        # Foreach control panel, disable toggle button depending on power
        for ctl in self.controlPanels:
            ctl.button.configure(state="active" if self.statusBool else "disabled")
            # When toggling power, always turn control panels off
            ctl.toggleStatus(False)

class ControlPanel:
    def __init__(self, master, gpio):
        self.statusBool = False
        self.master = master
        self.label = gpio
        self.gpio = gpio
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = gpio)
        self.text.grid(row=0, column=0, pady=10)

        # Status
        self.status = Label(self.frame, bg="red", width=10)
        self.status.grid(row=2, column=0, pady=10)

        # Toggle Button
        self.button = Button(self.frame, text = "Toggle", command=lambda : self.toggleStatus(not self.statusBool), state="disabled")
        self.button.grid(row=1, column=0, pady=10)

        self.frame.pack()
    
    def toggleStatus(self, newStatus):
        self.statusBool = newStatus
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