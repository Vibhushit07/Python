import tkinter as tk

class tempConverter(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title("Temperature Converter")
        self.master.geometry('500x300')
        self.create_widgets()

    def convertTemp(self):
        # x = self.z.get()
        # y = self.tem.get()
    
        # if y == '°C':
        #     d = (x * 9 / 5) + 32
        #     self.output_label.config(text = "%.1f Farheinheit" % d)
        # elif y == '°F':
        #     d = (x - 32 ) * 5 / 9
        #     self.output_label.config(text = "%.1f Celsius" % d)

        temprature = 0.0

        if self.tem.get() == "°C":
            if self.temp.get() == "°C":
                temprature = self.value.get()

            elif self.temp.get() == "°F":
                temprature = (self.value.get() * 9 / 5) + 32

            elif self.temp.get() == "K":
                temprature = self.value.get() + 273.15

            elif self.temp.get() == "°Ra":
                temprature =  (self.value.get() * 9 / 5) + 491.67
            else:
                temprature = self.value.get() * 0.8

        elif self.tem.get() == "°F":
            if self.temp.get() == "°C":
                temprature = (self.value.get() - 32) * 5 / 9

            elif self.temp.get() == "°F":
                temprature = self.value.get()

            elif self.temp.get() == "K":
                temprature = (self.value.get() - 32) * 5 / 9 + 273.15

            elif self.temp.get() == "°Ra":
                temprature =  self.value.get() + 459.67
            else:
                temprature = (self.value.get() - 32) * 4 / 9

        elif self.tem.get() == "K":
            if self.temp.get() == "°C":
                temprature = self.value.get() - 273.15

            elif self.temp.get() == "°F":
                temprature = (self.value.get() - 273.15) * 9 / 5 + 32

            elif self.temp.get() == "K":
                temprature = self.value.get()

            elif self.temp.get() == "°Ra":
                temprature =  self.value.get() * 1.8
            else:
                temprature = (self.value.get() - 273.15) * 0.8

        elif self.tem.get() == "°Ra":
            if self.temp.get() == "°C":
                temprature = (self.value.get() - 491.67) / 1.8

            elif self.temp.get() == "°F":
                temprature = self.value.get() - 459.67

            elif self.temp.get() == "K":
                temprature = self.value.get() / 1.8

            elif self.temp.get() == "°Ra":
                temprature =  self.value.get()
            else:
                temprature = (self.value.get() - 491.67) * 4 / 9
            
        else:
            if self.temp.get() == "°C":
                temprature = self.value.get() / 0.8

            elif self.temp.get() == "°F":
                temprature = (self.value.get() * 9 / 4) + 32

            elif self.temp.get() == "K":
                temprature = (self.value.get() - 32) * 5 / 9 + 273.15

            elif self.temp.get() == "°Ra":
                temprature =  (self.value.get() * 5 / 4) + 273.15
            else:
                temprature = self.value.get()

        
        self.output_label.config(text = "%.2f " % temprature)

    def create_widgets(self):
        
        self.label = tk.Label(self.master, text = "Temperature Converter", font = "Arial 12 bold")
        self.label.place(x = 150, y = 20)
        self.value = tk.IntVar()

        self.entry = tk.Entry(self.master, width = 20, textvariable = self.value)
        self.entry.grid(row = 0, column = 0, padx = 40, pady = 70)
        
        optionlist = ["°C", "°F", "K", "°Ra", "°Re"]

        self.tem = tk.StringVar()
        self.tem.set("°C")
        self.fromUnit = tk.OptionMenu(self.master, self.tem, *optionlist)
        self.fromUnit.grid(row = 0, column = 1)

        self.to = tk.Label(self.master, text = "To", font = "Arial 12 bold")
        self.to.place(x = 345, y = 70)
        
        self.temp = tk.StringVar()
        self.temp.set("°C")

        self.toUnit = tk.OptionMenu(self.master, self.temp, *optionlist)
        self.toUnit.grid(row = 0, column = 2)

        self.output_label = tk.Label(text = "", width = 20)
        self.output_label.grid(row = 1, column = 1, padx = 20, pady = 20)
        self.conv = tk.Button(self.master, text = "Convert", command = self.convertTemp)
        self.conv.grid(row = 1, column = 0, padx = 50, pady = 30)
    
root = tk.Tk()
app = tempConverter(master = root)
app.mainloop()