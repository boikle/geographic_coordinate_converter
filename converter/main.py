from tkinter import Tk, Label, Entry, Button
import tkinter.scrolledtext as tkscroll

class Converter:
    '''
    Class: Converter
    Description: UI for converting geographic coordinates into various formats
    '''
    def __init__(self, window):
        self.window = window
        window.resizable(width=False, height=False)
        window.geometry('480x220')
        window.title("Geographic Coordinate Converter")

        self.lat_label = Label(window, text="Latitude").grid(row=0, pady=2)
        self.long_label = Label(window, text="Longitude").grid(row=1, pady=2)

        self.lat = Entry(window, width=50)
        self.long = Entry(window, width=50)

        self.lat.grid(row=0, column=1)
        self.long.grid(row=1, column=1)

        self.convert_button = Button(window, text="Convert", command=self.convert).grid(row=2, columnspan=2, pady=5)

        self.result = tkscroll.ScrolledText(window, width=55, height=6).grid(row=3, columnspan=2, padx=2, pady=2)

    def convert(self):
        '''Future convert function code'''
        print("Converting Coordinates")

root = Tk()
converter_ui = Converter(root)
root.mainloop()
