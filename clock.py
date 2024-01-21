import tkinter as tk
import time

def update_clock():
    ora_curenta = time.strftime("%H:%M:%S")
    ceas.config(text=ora_curenta)
    ceas.after(1000, update_clock)


app = tk.Tk()
app.title("ilD1k clock")

ceas = tk.Label(app, text="", font=("ild1k" , 50))
ceas.pack()

update_clock()
app.mainloop()
