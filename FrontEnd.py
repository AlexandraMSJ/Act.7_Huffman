from tkinter import filedialog
from tkinter import ttk
import tkinter
from collections import Counter

def abrir_archivo():
    # Función para abrir el archivo
    archivo = filedialog.askopenfile(mode='r')
    if archivo:
        # Leer el contenido del archivo seleccionado
        contenido = archivo.read()
        archivo.close()
        
        # Contar caracteres y calcular frecuencia
        caracteres = contar_carac(contenido)
        frecuencia = ordenar_caracteres(contenido)
        
        # Mostrar resultados en una ventana emergente
        ventana_resultados = tkinter.Tk()
        ventana_resultados.title("Resultados")
        
        ttk.Label(ventana_resultados, text=f"Número de caracteres: {caracteres}").pack()
        ttk.Label(ventana_resultados, text="Frecuencia de caracteres:").pack()
        for caracter, freq in frecuencia:
            ttk.Label(ventana_resultados, text=f"Caracter: {caracter}, Frecuencia: {freq}").pack()
        
        ventana_resultados.mainloop()

def comprimir_archivo():
    # Funcion para comprimir
    pass

def descomprimir_archivo():
    # Función para descomprimir
    pass

def contar_carac(mensaje):
    # Contar los caracteres
    return len(mensaje)

def ordenar_caracteres(mensaje):
    # Ordenar caracteres por frecuencia
    carac_rep = Counter(mensaje)
    return sorted(carac_rep.items(), key=lambda x: x[1], reverse=True)

# Crear ventana
ventana = tkinter.Tk()
ventana.title("Compresión de Archivos")

# Posición de los botones
frm = ttk.Frame(ventana, padding=10)
frm.grid(column=0, row=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)

ttk.Label(frm, text="Selecciona un archivo:").grid(column=0, row=0, pady=5)
boton_examinar = ttk.Button(frm, text="Examinar", command=abrir_archivo)
boton_examinar.grid(column=0, row=1, pady=5)

ttk.Label(frm, text="Comprimir archivo:").grid(column=0, row=2, pady=5)
boton_comprimir = ttk.Button(frm, text="Comprimir", command=comprimir_archivo)
boton_comprimir.grid(column=0, row=3, pady=5)

ttk.Label(frm, text="Descomprimir archivo:").grid(column=0, row=4, pady=5)
boton_descomprimir = ttk.Button(frm, text="Descomprimir", command=descomprimir_archivo)
boton_descomprimir.grid(column=0, row=5, pady=5)

# Se inicia la ventana
ventana.mainloop()
