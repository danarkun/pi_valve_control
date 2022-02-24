from tkinter import *
from turtle import width
# import RPi.GPIO as GPIO

VALVE1 = "VALVE 1"
VALVE2 = "VALVE 1"
VALVE3 = "VALVE 3"

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

        cp1 = ControlPanel(ctl1Frame, VALVE1, GPIO_VALVE1)
        ctl1Frame.grid(row=1, column=0)

        cp2 = ControlPanel(ctl2Frame, VALVE2, GPIO_VALVE2)
        ctl2Frame.grid(row=1, column=1)

        cp3 = ControlPanel(ctl3Frame, VALVE3, GPIO_VALVE3)
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
    def __init__(self, master, valve, gpio):
        self.master = master
        self.statusBool = False
        self.valve = valve
        self.label = gpio
        self.gpio = gpio
        self.frame = Frame(self.master)

        # Label
        self.text = Label(self.frame, text = '{}({})'.format(valve, gpio))
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

    def toggle_fs(dummy=None):
        state = False if gui.attributes('-fullscreen') else True
        gui.attributes('-fullscreen', state)
        if not state:
            gui.geometry('480x320+100+100')

    gui.attributes('-fullscreen', True)
    gui.bind('<Escape>', toggle_fs)

    gui.mainloop()

if __name__ == "__main__":
    main()