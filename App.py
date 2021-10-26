import tkinter as tk
import secure

def passwin():
    passwin = tk.Tk()
    passwin.title("Pasword")
    width=253
    height=59
    screenwidth = passwin.winfo_screenwidth()
    screenheight = passwin.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    passwin.geometry(alignstr)
    passwin.resizable(False,False)

    passentry=tk.Entry(passwin,borderwidth="1px",fg="#333333",justify="center",textvariable="password",show="*")
    passentry.place(x=10,y=10,width=183,height=36)

    def savebutton():
        ths = open("password.txt", "w")
        ths.write(secure.encode(passentry.get())),
        ths.close()

    passbutton=tk.Button(passwin,bg="#f0f0f0",fg="#000000",justify="center",text="Save",command=savebutton)
    passbutton.place(x=200,y=10,width=45,height=36)

    passwin.mainloop()
    passentry.pack()
    passbutton.pack()

