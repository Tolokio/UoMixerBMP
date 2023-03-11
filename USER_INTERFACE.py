import tkinter as tk
from tkinter import messagebox
import os

def ejecutar_archivo1():
    os.system("ANIM1+ANIM2.py")
    
def ejecutar_archivo2():
    os.system("ANIM1-ANIM2.py")
    
def ejecutar_archivo3():
    os.system("ANIM1-ANIM2Outline.py")
    
def ejecutar_archivo4():
    #os.system("python archivo2.py")
    print("not implemented yet")
    
def ejecutar_archivo5():
    #os.system("python archivo2.py")
    print("not implemented yet")

#def ejecutar_archivo6():
#    os.system("Convert_BMPtoPNG.py")

#def ejecutar_archivo7():
#    os.system("Convert_PNGtoBMP.py")

def ejecutar_archivo8():
    os.system("CREATE_FOLDERS.py")

def ejecutar_archivo9():
    os.system("ANIM1_EMPTIER.py")

def ejecutar_archivo14():
    os.system("ANIM1_EMPTIER-white.py")

def ejecutar_archivo10():
    os.system("ANIM1y2_WHITES_TO_BLACK.py")


def ejecutar_archivo11():
    os.system("ANIM1-ANIM2-white.py")

def ejecutar_archivo12():
    os.system("ANIM1-ANIM2Outline-white.py")

def ejecutar_archivo15():
    os.system("ANIM1y2_BLACKS_TO_WHITE.py")

def salir():
    salir = messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?")
    if salir:
        ventana.destroy()

ventana = tk.Tk()
ventana.title(":3")
ancho_actual = ventana.winfo_width()
ventana.geometry(str(200) + "x" + str(430) + "+0+0")

lbl1 = tk.Label(ventana, text="", )
lbl1.pack()
boton8 = tk.Button(ventana, text="CREATE FOLDERS", command=ejecutar_archivo8)
boton8.pack()
lbl2 = tk.Label(ventana, text="", )
lbl2.pack()
boton1 = tk.Button(ventana, text="ANIM1 + ANIM2", command=ejecutar_archivo1)
boton1.pack()
lbl3 = tk.Label(ventana, text="", )
lbl3.pack()
lbl4 = tk.Label(ventana, text="BLACK BACKGROUND", )
lbl4.pack()
boton2 = tk.Button(ventana, text="ANIM1 - ANIM2", command=ejecutar_archivo2)
boton2.pack()
boton3 = tk.Button(ventana, text="ANIM2 - A2outline", command=ejecutar_archivo3)
boton3.pack()
boton9 = tk.Button(ventana, text="EMPTY ANIM1", command=ejecutar_archivo9)
boton9.pack()
boton10 = tk.Button(ventana, text="Anim1&2WhitesToBlack", command=ejecutar_archivo10)
boton10.pack()
lbl5 = tk.Label(ventana, text="", )
lbl5.pack()
lbl6 = tk.Label(ventana, text="WHITE BACKGROUND", )
lbl6.pack()
boton11 = tk.Button(ventana, text="ANIM1 - ANIM2", command=ejecutar_archivo11)
boton11.pack()
boton12 = tk.Button(ventana, text="ANIM2 - A2outline", command=ejecutar_archivo12)
boton12.pack()
boton14 = tk.Button(ventana, text="EMPTY ANIM1", command=ejecutar_archivo14)
boton14.pack()
boton15 = tk.Button(ventana, text="Anim1&2BlacksToWhite", command=ejecutar_archivo15)
boton15.pack()
lbl7 = tk.Label(ventana, text="", )
lbl7.pack()
boton100 = tk.Button(ventana, text="QUIT", command=salir)
boton100.pack()

ventana.mainloop()
