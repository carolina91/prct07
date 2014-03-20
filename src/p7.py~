#!/usr/bien/python
#!enconding: UTF-8
import modulo

tupla= (10,20,30,40)
lista= []
for i in tupla:
  valor_pi = modulo.calcular_pi (i)
  lista.append (valor_pi)
print lista

pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT)
  
  
dif35 = []
for i in range (len (tupla)):  
  dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
for i in range (len (tupla)):
   print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,pi35[i],lista[i],dif35[i])
 

#(eso es para que no imprima un enter al final sino que siga en la misma linea) 
 #PARA SABER MAS
print "Pasando la salida a una matriz..."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #    
matriz = []
for i in range (len(tupla)):
  matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len(tupla)):
  print
  print matriz[i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #
    
    
    
    
    
    
    
#ejercicios
#1. creamos el archivo modulo que realiza lo que se pide (practica 6)y desde el archivo p7 llamamos al codigo y utilizamos el codigo 2.
#2 el numero maximo de elementos de la t-upla depende de la memoria de cada maquina. se producen errires oara los elementos demasiado grandes, lo que habra que escribirlos en notacion cientifica. la extension pyc podra ser reconocida dependiendo de la utilizacion del if __name__="__main__"
#3 hay que añadir la funcion time al for para  que diga el tiempo que tarda cada iteracion