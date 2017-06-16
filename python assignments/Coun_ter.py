import tkinter
import My_Frame




class Counter:
    """
     class Counter is the MODEL for a simple program that exemplifies the Model/View/Controller architecture. It just maintains a counter that starts at 0 and is incremented each time the inc() method is called.

     In a real MVC app, the Model would contain all the business logic. Note that the Model never contains a reference to the View.
     """
    def __init__(self):
        """
        sets both tempEntryFarenheit and tempEntryCelsius to 0
        """
        self.tempEntryFarenheit = 0
        self.tempEntryCelsius = 0

    def ConvertToCelsius(self, input):
        """
        converts input temperature to celsius
        """

        input = float(input)
        if input != 0.0:
            celsius = (input - 32) * 5 / 9
        else:
            celsius = -17.7777778
        return celsius

    def ConvertTofarenheit(self, input ):
        """
        converts input temperature to celsius
        """
        input = float(input)
        if input != 0.0:
            fahrenheit = ((9/5)*input)+32
        else:
            fahrenheit = 32
        return  fahrenheit


