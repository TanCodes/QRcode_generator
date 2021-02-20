import pyqrcode
from tkinter import *
from tkinter import messagebox

t = Tk()
t.title("QRcode Generator")
t.geometry("300x100")

def click():
    gett = enter.get()
    if not gett:
        messagebox.showerror("Data error","Can't keep empty")
    else:
        code = pyqrcode.create(gett)

        #saving to qr.svg
        code.svg("qr.svg", scale=8)

        #saving to qr.png
        code.png('qr.png', scale=6)

        messagebox.showinfo("Saved", "Image is saved in png and svg!")

L1 = Label(t,text="Enter your text :", font=("poppins",9) , bg="#48b1f7" ,fg="#ffffff")
L1.place(x = 20, y = 13)

var1 = StringVar()
enter = Entry(t,  width="25" )
enter.place(x=120,y=15)

but = Button(t,text="Generate",font=("poppins",9), fg="red",width=25,relief="raised", command = click)
but.place(x=55,y=45)

L2 = Label(t,text=">_TanCodes" , font=("poppins",7),bg="#c5dae8", border="2")
L2.place(x = 120, y = 80)

t.resizable(0,0)
t.configure(background='#f2fcff')
t.mainloop()

