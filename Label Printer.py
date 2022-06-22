import tkinter as tk
import random

class color_label(tk.Tk):
    master_colour_list = ["red","orange","yellow","green","blue","purple", "black", "white"]
    def __init__(self):
        tk.Tk.__init__(self)
        self.colour_list = color_label.master_colour_list[:]
        self.entry = tk.Entry(self)
        self.entry.insert(0, "Type stuff here!")
        self.entry2 = tk.Entry(self)
        self.entry2.insert(0, 3)
        self.button = tk.Button(text='Print Label', command=self.on_button)
        self.entry.pack()
        self.entry2.pack()
        self.button.pack()

    def create_label(self, words):
        self.label = tk.Label(
            text = words,
            foreground = random.choice(self.colour_list),
            background = random.choice(self.colour_list),
        )
        if self.label.cget("foreground") == self.label.cget("background"):
            print("Whoops")
            return self.create_label(words)
            
        self.label.pack()

    def print_label(self,num,words):
        for x in range(0,num):
            self.create_label(words)
            
    def on_button(self):
        cl.print_label(int(self.entry2.get()),self.entry.get())

cl = color_label()
cl.mainloop()

print("Done")
