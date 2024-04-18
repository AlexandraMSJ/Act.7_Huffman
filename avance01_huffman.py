from tkinter import filedialog
from tkinter import ttk
import tkinter

def abrir_archivo():
    archivo = tkinter.filedialog.askopenfile(mode='r')

#abrir ventana
ventana = tkinter.Tk()
frm = ttk.Frame(ventana, padding=10)
boton = ttk.Button(ventana, text="Seleccionar archivo", command=abrir_archivo)
archivo = tkinter.filedialog.asksaveasfile(mode='w')
boton.pack()
ventana.mainloop()
