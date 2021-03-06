from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

#-------------Variables Globales---------
operacion = ""
resultado = 0
decimal = 0

#----------Pantalla ------------------------

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


#----------Pulsaciones Teclado -------------------

def numeroPulsado(num):

    global operacion

    if operacion != "":

        numeroPantalla.set(num)
        operacion = ""
    else:

        numeroPantalla.set(numeroPantalla.get() + num)
#------------ Funcion Suma ---------------


def suma(num):

    global operacion
    global resultado
    global decimal


    resultado += float(num)
    numeroPantalla.set(resultado)


    operacion = "suma"
    decimal = 0

    print (resultado)
    print (operacion)



#---------------Funcion Resta---------------------

def resta(num):

    global operacion
    global resultado
    global decimal

    print ("dentro resta")
    print (operacion)


    if resultado>0:

        calcular("suma", num)

    else:
        resultado = resultado - float(num)
        numeroPantalla.set(resultado)

    operacion = "resta"
    decimal = 0
    print (resultado)
    print (operacion)


#-------------Funcion Calcular--------------------

def calcular(operation,num):

    global resultado
    global decimal


    print ("dentro operacion")
    print (operation)
    print (num)
    print (resultado)
    print (operation)
    if operation == "suma":
        print ("restando")
        resultado += float(num)
    elif operation == "resta":
        print("sumando")
        resultado -= float(num)
    elif operation == "multiplicar":
        resultado = resultado * float(num)
    else:
        resultado = resultado / float(num)

    decimal = 0
    numeroPantalla.set(resultado)


#----------Funcion el_resultado---------------------

def el_resultado():

    global resultado
    global decimal

    numeroPantalla.set(resultado + float(numeroPantalla.get()))
    resultado = 0

    decimal = 0

    global operacion
    operacion = "suma"


#---------------Funcion punto_decimal--------------

def punto_decimal():

    global decimal

    if decimal == 0:
         numeroPantalla.set(numeroPantalla.get() + ".")

         decimal += 1

#------------Funcion Borrar-------------------

def borra_memoria():

    global resultado

    global operacion

    global decimal

    operacion = ""

    operacion = ""
    resultado = 0
    decimal = 0
    numeroPantalla.set("")



#--------------Fila 1-----------------------

boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

botonDiv = Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#--------------Fila 2-----------------------

boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

botonMult = Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#--------------Fila 3-----------------------

boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

botonRest = Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

#--------------Fila 4-----------------------

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)

botonComa = Button(miFrame, text=",", width=3, command=lambda:punto_decimal())
botonComa.grid(row=5, column=2)

botonIgual = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)

botonSum = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

#-------Fila 5 ------------------------

botonBorrar = Button(miFrame, text="Borrar", width=3, command=lambda:borra_memoria())
botonBorrar.grid(row=6, column=4)


raiz.mainloop()