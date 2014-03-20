#!/usr/bien/python
#!enconding: UTF-8
import sys
import math


PI35DT= 3.1415926535897931159979634685441852

#utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
 xi = (i - 1.0/2.0) / n
 return xi
 
 #utilizacion de una funcion calcular_pi
def calcular_pi(n):
   PI35 = 3.1415926535897931159979634685441852
   sumatorio = 0.0
   ini = 0
   intervalos = 1.0 / float (n)
   for i in range(n):
     x_i = ((i+1) - 1.0/2.0) / n
     fx_i = 4.0 / (1.0 + x_i * x_i)
     ini += intervalos
     sumatorio += fx_i
   valor_pi = sumatorio / n
   return (valor_pi)
 
if(__name__=="__main__"): 
#programa principal
 argumentos = sys.argv[1:] #desde la posicion uno hasta el final
 print argumentos
 if (len(argumentos) == 2):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
 else:
    print "introduzca el numero de intervalos (n > 0):"
    n = int (raw_input())
    print "introduzca el numero de aproximaciones:"
    aproximaciones = int (raw_input())
 if (n>0): 
   PI35DT= 3.1415926535897931159979634685441852
   intervalo = n
   lista = [] #es una variable de tipo lista, con los corchetes ya lo estaria indicando
   for i in range (aproximaciones): #repita aproximaciones veces 
     valor = calcular_pi (intervalo)
     lista.append (valor) # el append es paara ir aniadiendo los valores que vayas poniendo a la lista, por ejeplo si pones
     intervalo += n       #valor =20 la lista seria [20] y si pones valor=10 entonces pasaria a ser [20,10] y asi sucesivamente
   print lista
#PARA SABER MAS
   diferencia = []
   for i in range (aproximaciones):
     dif = abs (PI35DT - lista[i])
     diferencia.append (dif)
   print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
   for i in range (aproximaciones):
     print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista[i],diferencia[i])
 else:
   print "el valor de los intervalos debe ser mayor que cero"