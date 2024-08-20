
import tkinter as tk
from client.gui_app import *

def main():
    root = tk.Tk()
    root.config(width=900)
    root.title('GEAA')
    root.iconbitmap('img/logo.png')
    root.resizable(0,0)

    barra_menu(root)
    app = Frame(root=root)

    app.mainloop()

if __name__ == '__main__':
    main()