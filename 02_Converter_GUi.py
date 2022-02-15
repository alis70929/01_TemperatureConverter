from functools import partial
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
                                          font="Arial 16 bold",
                                          bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        self.temp_instructions_label = Label(self.converter_frame, text="Instruction",
                                             font="arial 10 italic", bg=background_color)
        self.temp_instructions_label.grid(row=1)

        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=3)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font="Arial 10 bold",
                                  bg=background_color)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg=background_color)
        self.to_f_button.grid(row=0, column=1)

        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10)
        self.converted_label.grid(row=4)

        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5)

        self.calc_his_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                      text="Calculation History", width=15)
        self.calc_his_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=15, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "medium purple"

        # dsiable help button
        partner.help_button.config(state=DISABLED)

        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Heading
        self.help_heading = Label(self.help_frame, text="help / instructions",
                                  font="arial 10 bold", bg=background)
        self.help_heading.grid(row=0)
        # Text
        self.help_text = Label(self.help_frame, text="example text",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # DismissButton
        self.help_dismiss = Button(self.help_frame, text="dismiss",
                                   width=10, bg=background, font="arial 10 bold",
                                   command=partial(self.close_help, partner))
        self.help_dismiss.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
