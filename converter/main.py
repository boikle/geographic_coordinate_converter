from tkinter import Tk, Frame, Label, Entry, Button, Radiobutton, LEFT, X, TOP, BOTH, StringVar

import tkinter.scrolledtext as tkscroll

class Converter:
    '''
    Class: Converter
    Description: UI for converting geographic coordinates into various formats
    '''
    def __init__(self, window):
        window.resizable(width=False, height=False)
        window.geometry('480x220')
        window.title("Geographic Coordinate Converter")

        self.pane = Frame(window)
        self.pane.pack(fill=BOTH, expand=True)

        self.lat_frame = Frame(self.pane, pady=2, width=480)
        Label(self.lat_frame, text="Latitude").pack(side=LEFT, padx=6)
        Entry(self.lat_frame, width=50).pack(side=LEFT)
        self.lat_frame.pack(side=TOP)

        self.long_frame = Frame(self.pane)
        Label(self.long_frame, text="Longitude").pack(side=LEFT)
        Entry(self.long_frame, width=50).pack(side=LEFT)
        self.long_frame.pack(side=TOP)

        # Create a radio button variable with initalized value.
        self.coordsys = StringVar()
        self.coordsys.set('dd')

        self.radiobtn_frame = Frame(self.pane)
        Radiobutton(self.radiobtn_frame, text="DD", variable=self.coordsys, value="dd").pack(side=LEFT)
        Radiobutton(self.radiobtn_frame, text="DM", variable=self.coordsys, value="dm").pack(side=LEFT)
        Radiobutton(self.radiobtn_frame, text="DMS", variable=self.coordsys, value="dms").pack(side=LEFT)
        self.radiobtn_frame.pack(side=TOP)

        self.result = tkscroll.ScrolledText(self.pane, width=55, height=6)
        self.result.pack(side=TOP, fill=X, expand=True)

        self.convert_button = Button(self.pane, text="Convert", command=self.convert)
        self.convert_button.pack(side=TOP)

    def convert(self):
        '''Future convert function code'''
        print("Converting Coordinates")

root = Tk()
converter_ui = Converter(root)
root.mainloop()
