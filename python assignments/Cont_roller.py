import tkinter


import My_Frame
import Coun_ter


class ControllerTemp:

    """
    The CONTROLLER for an app that follows the MODEL/VIEW/CONTROLLER architecture.
    When the user presses a button on the VIEW,
    this controller calls the appropriate methods in the model.
    The controller handles all the communication between the model and the view.
    """

    def __init__(self):

        """
        This starts the TK framework up;
        instantiates the model;
        instantiates the VIEW;
        and states the event loop that waits for the user to press a button on the view
        """
        root = tkinter.Tk() #This starts the TK framework up;
        self.model = Coun_ter.Counter() #instantiates the model
        self.view = My_Frame.MyFrame(self) #instantiates the VIEW
        self.view.mainloop() # states event loop waits for user to press button on view
        root.destroy() #lets user quit

    def celsiusToFarenheit(self):
        """
        used to display the result temperature in farenheit to user
        """
        print((self.view.tempEntry.get()))
        result = self.model.ConvertTofarenheit(self.view.tempEntry.get())

        self.view.tempEntry.delete(0)
        self.view.tempEntry.insert(0, result)

    def farenheitToCelsius(self):
        """
        used to display the result temperature in celsius to user
        """
        print((self.view.tempEntry.get()))
        result = self.model.ConvertToCelsius(self.view.tempEntry.get())

        self.view.tempEntry.delete(0)
        self.view.tempEntry.insert(0, result)



if __name__=="__main__":
    c = ControllerTemp()