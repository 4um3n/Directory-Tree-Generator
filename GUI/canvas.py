from tkinter import Tk


def setup():
    root = Tk()
    root.title('Directory Tree Generator')
    root.configure(bg='gray10')
    root.geometry('800x800+0+0')
    root.wm_resizable(False, False)
    return root



