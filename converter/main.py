from tkinter import Tk, Label, Entry, Button

class Converter:
    '''
    Class: Converter
    Description: UI for converting geographic coordinates into various formats
    '''
    def __init__(self, master):
        self.master = master
        master.title("Geographic Coordinate Converter")

        self.lat_label = Label(master, text="Latitude")
        self.lat_label.pack()

        self.lat = Entry(master)
        self.lat.pack()

        self.long_label = Label(master, text="Longitude")
        self.long_label.pack()

        self.long = Entry(master)
        self.long.pack()

        self.convert_button = Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        '''Future convert function code'''
        print("Converting Coordinates")

root = Tk()
converter_ui = Converter(root)
root.mainloop()
