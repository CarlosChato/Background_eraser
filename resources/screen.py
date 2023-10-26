import tkinter as tk
from tkinter import Entry, Label, messagebox, ttk
from tkinter.filedialog import askopenfilenames,askopenfile
from tkinter.constants import SINGLE
from rembg import remove, new_session

class MyApp(tk.Tk):
    def __init__(self, parent=None):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.my_progress = ttk.Progressbar(orient='horizontal', length=300, mode='determinate')
        self.init_ui()
        self.files_input = []
        
    def init_ui(self):
        self.parent.title("Background remover")

        label_info = tk.Label(text='selecciona las imágenes que quieras y una vez seleccionadas dele a transformar',
                              font=18,background="AntiqueWhite3")
        
        button_mult_files = tk.Button(text='Open multiple images', width=20, height=2,
                                command=lambda:self.select_files())
        
        button_start_remove = tk.Button(text='Start removing', width=20, height=2,
                                        command=lambda:self.remover())
                
        label_info.grid(pady=5,padx=50)
        button_mult_files.grid(pady=120,padx=5)
        button_start_remove.grid(pady=15,padx=5)
        self.my_progress.grid(pady=80, padx=5)

    def select_files(self):
        self.files_input = askopenfilenames()
        print(self.files_input)
        self.my_progress["value"] = 0

    def remover(self):
        session = new_session()
        print(self.files_input)

        percent = len(self.files_input)
        percent = 100 / percent

        f = lambda x: x.split('.')[0]+'_out.'+x.split('.')[1]

        for n in self.files_input:
            print(n)
            with open(n,'rb') as i:
                
                print(f(n))
                with open(f(n), 'wb') as o:
                    input = i.read()
                    out = remove(input,session)
                    o.write(out)

            self.my_progress["value"] += percent
        

            

        