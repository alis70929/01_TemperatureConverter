from functools import partial
from tkinter import *
# from functools import partial # to prevent unwanted windows(duplicates)


class Converter:
    # Initialization of converter
    def __init__(self, parent):

        # Formatting Variables
        background_color = "light blue"
        
        self.all_calculations = []
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
                                  bg=background_color, padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg=background_color, padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10)
        self.converted_label.grid(row=4)

        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5)

        self.calc_his_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                      text="Calculation History", width=15,
                                      command=self.history)
        self.calc_his_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=15, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def temp_convert(self, low):
        error_color = "#ffafaf"
        to_convert = self.to_convert_entry.get()
        print()
        print("{} to convert".format(to_convert))
        print("{} is low boundary".format(low))

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{}degrees C is {} Degrees F".format(to_convert, fahrenheit)

            elif low == -459 and to_convert >= low:
                Celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                Celsius = self.round_it(Celsius)
                answer = "{} degrees F is {} Degrees C".format(to_convert, Celsius)

            else:
                answer = "Too Cold!"
                has_errors = "yes"

            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error_color)

            if answer != "Too Cold!":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.converted_label.configure(text="Enter a Number!!!", fg="red")
            self.to_convert_entry.configure(bg=error_color)
            print("error")

    def history(self):
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")

    def round_it(self, to_round):
        if to_round % 1 == 0:
            return int(to_round)
        else:
            return round(to_round, 1)


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


class History:
    def __init__(self, partner):
        background_color = "#a9ef99"
        partner.calc_his_button.config(state=DISABLED)

        self.history_box = Toplevel()

        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, bg=background_color)
        self.history_frame.grid()

        self.history_header = Label(self.history_frame, text="history / Instructions",
                                    font="arial 14 bold", bg=background_color)
        self.history_header.grid(row=0)

        self.history_text = Label(self.history_frame,
                                  text="here are your most recent calculations"
                                  "please use the export button to create a text file"
                                  "of all your calculations for this session",
                                  font="arial 10 italic", justify=LEFT,
                                  bg=background_color, fg="maroon", padx=10, pady=10)
        self.history_text.grid(row=1)

        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 10 bold")
        # DismissButton
        self.history_dismiss = Button(self.export_dismiss_frame, text="dismiss",
                                      width=10, bg=background_color, font="arial 10 bold",
                                      command=partial(self.close_history, partner))
        self.history_dismiss.grid(row=0, column=1, pady=10)

    def close_history(self, partner):
        partner.calc_his_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
