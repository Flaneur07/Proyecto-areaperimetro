from tkinter import *



def operacion():
    resultado_a.set(3.14* int(radio.get())**2)
    borrar()
def perimetro():
    resultado_a.set(3.14*2 * int(radio.get()))
    borrar()

def borrar():
    radio.set("")





root = Tk()

root.title("Calculadora A.P")
root.resizable(1,1)


radio = StringVar()
resultado_a = StringVar()




#Formula para perímetro. 
# def calculo():
    #perimetro = (2*pi)*(radio)
# area pi * radio**2

Label(root, text="Ingrese el radio:").pack()
Entry(root,justify="center",textvariable=radio).pack()

Label(root, text="resultado del circulo es:" ).pack()
Entry(root,justify="center",textvariable=resultado_a,state="disabled").pack()

Button(root,text="Calcular área",command=operacion).pack()
Button(root,text="Calcular perímetro",command=perimetro).pack()





root.mainloop()

