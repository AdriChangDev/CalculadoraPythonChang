class Miexception(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

import math
from fractions import Fraction
"""
Este metodo lo que hace es resolver una ecuacion de segundo grado 
"""
def ecuacion_segundo_grado(a, b, c):
    # Calcula el discriminante
    discriminante = (b**2) - (4*a*c)

    # Calcula las soluciones
    solucion1 = (-b-math.sqrt(discriminante))/(2*a)
    solucion2 = (-b+math.sqrt(discriminante))/(2*a)

    # Devuelve las soluciones en forma de fraccion
    return Fraction(solucion1).limit_denominator(), Fraction(solucion2).limit_denominator()



"""
Este es un metodo para hacer las Operaciones
te devuelve un numero
"""
def  operando(num1,num2,op):
    solucion=0
    if(op=="+"):
        solucion=num1+num2
    elif(op=="-"):
        solucion=num1-num2
    elif(op=="*"):
        solucion=num1*num2
    elif(op=="/"):
        solucion=num1/num2
    elif(op=="%"):
        solucion=num1%num2
    return solucion
   

"""
ESTE METODO TE HACE EL FUNCIONAMIENTO DE TODO EL PROYECTO
"""
b1 = False

while (b1==False):
    try:
        print("################################################################"
            "\n########### BIENVENIDO A LA CALCULADORA DE CHANG   #############"
            "\n################################################################")
        ope = input("¿Que Operacion Desea Realizar?"
                    "\n\t1)Suma"
                    "\n\t2)Restar"
                    "\n\t3)Multiplicar"
                    "\n\t4)Dividir"
                    "\n\t5)Resto"
                    "\n\t6)Raiz"
                    "\n\t7)Elevado"
                    "\n\t8)Otro tipo de Operaciones"
                    "\n\t9)Salir"
                    "\n\th)Ayuda"
                    "\n")
        if ope == "1":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para sumar\n"))
                    print("El numero elegido es: ",numero1)
                    numero2=int(input("Introduzca Numero 2 para sumar\n"))
                    resultado=operando(numero1,numero2,"+")
                    print("El resultado de la suma es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

           
        elif ope == "2":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para restar\n"))
                    print("El numero elegido es: ",numero1)
                    numero2=int(input("Introduzca Numero 2 para restar\n"))
                    resultado=operando(numero1,numero2,"-")
                    print("El resultado de la resta es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

        elif ope == "3":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para multiplicar\n"))
                    print("El numero elegido es: ",numero1)
                    numero2=int(input("Introduzca Numero 2 para multiplicar\n"))
                    resultado=operando(numero1,numero2,"*")
                    print("El resultado de la multiplicacion es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

        elif ope == "4":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para dividir\n"))
                    print("El numero elegido es: ",numero1)
                    numero2=int(input("Introduzca Numero 2 para dividir\n"))
                    resultado=operando(numero1,numero2,"/")
                    print("El resultado de la division es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

        elif ope == "5":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para dividir\n"))
                    print("El numero elegido es: ",numero1)
                    numero2=int(input("Introduzca Numero 2 para dividir\n"))
                    resultado=operando(numero1,numero2,"%")
                    print("El resto de la division es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

        elif ope == "6":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para realizar raiz\n"))
                    print("El numero elegido es: ",numero1)
                    resultado=math.sqrt(numero1)
                    print("El resultado de la raiz es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")

        elif ope == "7":
            numCorrecto=False
            while(numCorrecto==False):
                try:
                    numero1=int(input("Introduzca Numero 1 para realizar cuadrado:"))
                    print("El numero elegido es: ",numero1) 
                    resultado=math.pow(numero1,2)
                    print("El resultado del cuadrado es: ", str(resultado))
                    numCorrecto=True
                except Exception as e:
                    print("Debes meter numeros")
        elif ope == "8":
            
            b12=False
            while(b12==False):
                try:
                    ope2=input("Que quieres hacer?\n1)2ºGrado\n2)3erGrado\n3)Salir\n")
                    if(ope2=="1"):

                        print("La formula es ax^2+bx+c=0")
                        a=int(input("Introduzca a: "))
                        b=int(input("Introduzca b: "))
                        c=int(input("Introduzca c: "))
                        print("La solucion de ",a,"x²+", b ,"x+",c,"=0 es--> ",ecuacion_segundo_grado(a,b,c) )
                    elif(ope2=="2"):
                        print("La formula es ax³+bx²+cx+d=0")
                        a=int(input("Introduzca a: "))
                        b=int(input("Introduzca b: "))
                        c=int(input("Introduzca c: "))
                        d=int(input("Introduzca d: "))
                        print("La solucion de ",a,"x³+", b ,"x²+",c,"x+",d,"=0 es--> ",solve_cubic(a,b,c,d) )

                    elif(ope2=="3"):
                        b12=True
                    else:

                        print("Debes Meter numeros ")
                except Exception as e:
                    print("ERROR")
        elif ope == "9":
            print("Gracias por Usar mi Aplicacione")
            b1=True
        elif ope == "h":
            print("\nTodos los métodos te van a pedir dos numeros."
                  "\nSumar->Suma ambos numeros"
                  "\nRestar->Resta ambos numeros"
                  "\nMultiplicar->Multiplica ambos numeros"
                  "\nDividir->Divide el numero 1 entre el numero 2"
                  "\nResto->Devuelve el resto de la division"
                  "\nRaiz->Hace la raiz cuadrada del numero seleccionado"
                  "\nElevado->Eleva el numero al cuadrado"
                  "\nOtros->Muestra otros metodos distintos\n\n"

                  )
        elif ope == "H":
             print("\nTodos los métodos te van a pedir dos numeros."
                  "\nSumar->Suma ambos numeros"
                  "\nRestar->Resta ambos numeros"
                  "\nMultiplicar->Multiplica ambos numeros"
                  "\nDividir->Divide el numero 1 entre el numero 2"
                  "\nResto->Devuelve el resto de la division"
                  "\nRaiz->Hace la raiz cuadrada del numero seleccionado"
                  "\nElevado->Eleva el numero al cuadrado"
                  "\nOtros->Muestra otros metodos distintos\n\n"
                  )
        else:
            raise Miexception("Error: Debes meter un numero Valido")
    except Miexception as e:
        print(e.mensaje)
print("Si quieres saber  mas de mis trabajos te puedes meter a mi gitHub ->adrichxng._")


