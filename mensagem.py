from tkinter import messagebox

class Mensagem:
    def aletar(titulo: str = '', mensagem: str = ''):
        messagebox.showinfo(title=titulo, message=mensagem)
        