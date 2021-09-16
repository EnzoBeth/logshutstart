from tkinter import *
import os


def shutdown():
    return os.system("shutdown /s /t 1")


def restart():
    return os.system("shutdown /r /t 1")


def logout():
    return os.system("shutdown -l")


def shutui():
    return os.system("shutdown -i")



master = Tk()

master.geometry("380x155")
master.configure(bg='black')
master.resizable(False, False)
master.title('logshutstart - 0.0.1al')

Button(master, text="Shutdown", command=shutdown).place(x=20, y=20)
Button(master, text="Restart", command=restart).place(x=20, y=50)
Button(master, text="Logout", command=logout).place(x=20, y=80)
Button(master, text="Remote shutdown", command=shutui).place(x=20, y=110)
Label(master, text="Logshutstart 0.0.1 by EnzoBeth").place(x=180, y=110)


mainloop()
