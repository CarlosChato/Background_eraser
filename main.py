from resources.screen import MyApp
import tkinter as tk

if __name__=="__main__":
    # It initializates the App to mainloop it
    ROOT = tk.Tk()
    ROOT.geometry("700x700")
    ROOT.configure(background="AntiqueWhite3")
    APP = MyApp(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()