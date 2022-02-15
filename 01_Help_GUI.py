from tkinter import *
# from functools import partial # to prevent unwanted windows(duplicates)
import random


class Converter:
    # Initialization of converter
    def __init__(self, parent):

        # Formatting Variables
        background_color = "light blue"

        # converter main screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_color, padx=10, pady=10)
        self.converter_frame.grid()

        # Temerature Converter Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button Row 1
        self.help_button = Button(self.converter_frame, text="help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=2)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def _init_(self, partner):
        background = "purple"

        # dsiable help button
        partner.help_button.config(state=DISABLED)

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text="help / instructions",
                                  font="arial 10 bold", bg=background)
        self.help_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="example text",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        self.help_dismiss = Button(self.help_frame, text="dismiss")




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
