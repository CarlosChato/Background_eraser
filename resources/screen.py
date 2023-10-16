import tkinter as tk
from tkinter import Entry, Label, messagebox, ttk
from tkinter.filedialog import askopenfile
from tkinter.constants import SINGLE

class MyApp(tk.Tk):
    def __init__(self, parent=None):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Background remover")
        
        button_test = tk.Button(text="testing", width=20, height=2,
                                command=lambda:self.select_file())  
        
        button_test.grid(pady=25,padx=5)

    def select_file(self):
        #filename = askopenfile()
        print(12)