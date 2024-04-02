#second release of tablas_de_multiplicar.py
#this update includes 2 languages, contact & low & high values election
#release date (last edit): 11/03/2023 
from random import randint
from time import sleep
#language choice
b1 = True
print("If you have any comment or you found an issue, please contact me: joanalnu5@gmail.com")
print("Comming soon: modes")
print("")


while b1:
  l_election = input("Choose a language | Elige un lenguaje: ")
  if(l_election == "español" or l_election == "Español" or l_election == "1"):
    language = "español"
    b1 = False
  elif(l_election == "english" or l_election == "English" or l_election == "0"):
    language = "english"
    b1 = False
  else:
    print("Language not yet avaiable, you can choose another one:")
    b1 = True
print("")


#welcome
if language == "español":
  print("Hola, este es un entrenador de cálculo. Aquí podrás practicar las tablas de multiplicar.")
  print("Cuando un cálculo aparezca en tu pantalla, introduce la respuesta y haz clic en enter.")
  print("Si quieres terminar introduce '0' y haz clic en enter.")
  b3 = True
elif language == "english":
  print("Hello, this is a calculation trainer. Here you can practise the multiplication tables.")
  print("When a calculation appears in your display, type your answer and click enter.")
  print("If you want to stop, type '0' and click enter.")
  b3 = True
else:
  print("There was a problem with the language election. Please, restart the module or the script.")
print("")
  

#setting possible values for n1 & n2
while b3:
  if language == "español":
    print("Finalmente elige tus cifras")
    low = int(input("número más bajo: "))
    high = int(input("número más alto: "))
    if(low == 0 or high == 0) or (low == 0 and high == 0):
      print("'0' es un input invalido")
      print("")
      b3 = True
    elif low > high:
      auxiliar = low
      low = high
      high = auxiliar
      b = True
      b3 = False
    elif low == high:
      print("números iguales, invalido")
      print("")
      b3 = True
    else:
      b = True
      b3 = False
  elif language == "english":
    print("Finally, set you values")
    low = int(input("lowest number: "))
    high = int(input("highest number: "))
    if(low == 0 or high == 0) or (low == 0 and high == 0):
      print("'0' is an invalid input")
      print("")
      b3 = True
    elif low > high:
      auxiliar = low
      low = high
      high = auxiliar
      b = True
      b3 = False
    elif low == high:
      print("same numbers, invalid input")
      print("")
      b3 = True
    else:
      b = True
      b3 = False


c = 1
puntos = 0
while b:
  n1 = randint(low, high)
  n2 = randint(low, high)
  print(n1, "*", n2)
  ans = int(input())
  if(ans == n1*n2):
    puntos = puntos+1
    if language == "español":
      if(puntos == 1 or puntos == -1):
        if(c%2 == 0):
          print("¡¡Correcto!!  Tienes ", puntos, " punto")
        else:
          print("¡¡Muy bien!!  Tienes ", puntos, " punto")
      elif(puntos <-1 or puntos > 1 or puntos == 0):
        if(c%2 == 0):
          print("¡¡Correcto!!  Tienes ", puntos, " puntos")
        else:
          print("¡¡Muy bien!!  Tienes ", puntos, " puntos")
    elif language == "english":
      if(puntos == 1 or puntos == -1):
        if(c&2 == 0):
          print("Correct!! You have ", puntos, " point")
        else:
          print("Very good!! You have ", puntos, " point")
      elif(puntos < -1 or puntos > 1 or puntos == 0):
        if(c%2 == 0):
          print("Correct!! You have ", puntos, " points")
        else:
          print("Very good!! You have ", puntos, " points")
    c=c+1
    b = True
  elif(ans == 0):
      b = False
  else:
    puntos = puntos-1
    if language == "español":
      if(puntos == 1 or puntos == -1):
        print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " punto")
      elif(puntos < -1 or puntos > 1 or puntos == 0):
        print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " puntos")
    elif language == "english":
      if(puntos == 1 or puntos == -1):
        print("Oh no, incorrect!! You have ", puntos, " point")
      elif(puntos < -1 or puntos > 1 or puntos == 0):
        print("Oh no, incorrect!! You have ", puntos, " points")
    b = True

print("")
if language == "español":
  print("Gracias por jugar ¡¡Hasta la próxima!!")
elif language == "english":
  print("Thank you for playing, see you soon!!")
print("")
print("")
print("")

#kill()