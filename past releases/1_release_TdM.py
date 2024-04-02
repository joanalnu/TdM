#first release of tablas_de_multiplicar.py
#tablas de multiplicar (Pau)
from random import randint
from time import sleep
print("Hola, este es un entrenador de cálculo. Aquí podrás practicar las tablas de multiplicar del 1 al 10.")
print("Cuando aparezca una multiplicación introduce la respuesta y haz clic en enter. Tienes 10 segundos por cada respuesta.")
print("Si quieres para introduce '0' y haz clic en enter.")

#crear calculo random para los dos números de una multiplicación
c = 1;
puntos = 0;
b = True;
while b:
  n1 = randint(1, 10)
  n2 = randint(1, 10)
  print(n1, "*", n2)
  sleep(5)
  ans = int(input())
  #quitar lo del sleep y si ans es True
  if ans:
    if(ans == n1*n2):
      puntos = puntos+1
      if(puntos == 1 or puntos == -1):
        if(c%2 == 0):
          print("¡¡Correcto!!  Tienes ", puntos, " punto")
        else:
          print("¡¡muy bien!!  Tienes ", puntos, " punto")
      elif(puntos <-1 or puntos > 1):
        if(c%2 == 0):
          print("¡¡Correcto!!  Tienes ", puntos, " puntos")
        else:
          print("¡¡muy bien!!  Tienes ", puntos, " puntos")
      c=c+1
      b = True
    elif(ans == 0):
      b = False
    else:
      puntos = puntos-1
      if(puntos == 1 or puntos == -1):
        print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " punto")
      elif(puntos < -1 or puntos > 1):
        print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " puntos")
      b = True
  else:
    puntos = puntos-1
    if(puntos == 1 or puntos == -1):
      print("¡¡Sin tiempo!! Tienes ", puntos, "punto")
    elif puntos < -1 or puntos>1:
      print("¡¡Sin tiempo!! Tienes ", puntos, "puntos")
      b = True
print("Gracias por jugar ¡¡asta la próxima!!")
