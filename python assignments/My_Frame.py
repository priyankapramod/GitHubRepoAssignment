import tkinter
""" sets up a gui that accepts the temperature entered by the user and converts it to farenheit or celsius when
    respective button is pressed
"""

class MyFrame(tkinter.Frame):
    def __init__(self, controller):
        """
        class MyFrame is the VIEW for a simple program that exemplifies the Model/View/Controller architecture. This View class is a tkinter.Frame that contains two Buttons and a Label. One Button increments a counter and the other Button quits. The Label displays the current value of the counter. Notice that the View never contains a reference to the Model, but it does contain a reference to the Controller.

        """
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        """
        Instantiates all of the widgets and places them onto
        the frame
        """

        self.tempConverterLabel = tkinter.Label(self)
        self.tempConverterLabel["text"] = ("Enter Temperature:")
        self.tempConverterLabel.pack({"side":"left"})

        self.tempEntry = tkinter.Entry()
        self.tempEntry.insert(0, "0")
        self.tempEntry.pack({"side": "left"})



        self.farenheitButton = tkinter.Button(self)
        self.farenheitButton["text"] = "Convert to farenheit",
        self.farenheitButton["command"] = self.controller.celsiusToFarenheit
        self.farenheitButton.pack({"side": "left"})

        self.celsiusButton = tkinter.Button(self)
        self.celsiusButton["text"] = "Convert to Celsius",
        self.celsiusButton["command"] = self.controller.farenheitToCelsius
        self.celsiusButton.pack({"side": "right"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "right"})





