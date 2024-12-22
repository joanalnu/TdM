#TdM 3rd release
#contact: joanalnu5@gmail.com
from random import randint
from time import sleep

#i_problem (input problem)
def i_problem(language):
    if language == 0:
        print("A problem has ocurred, the program will restart in 5 seconds")
    elif language == 1:
        print("Ha habido un problema, el programa se reiniciará en 5 segundos")
    elif language == 2:
        print("Hi ha hagut un problema, el programa es reiniciarà en 5 segons")
    else:
        print("There's a problem with the language selection. The program will restart in 5 seconds. If the problem persists contact me: 'joanalnu5@gmail.com'")
    print("")
    sleep(5)
    main()

#language choice
def language_choice():
    l_election = input("First choose a language | Primero, elige un lenguaje | Primer escull una llengua : ")
    if(l_election == "español" or l_election == "Español" or l_election == "1" or l_election == "Epañol" or l_election == "Esañol" or l_election == "Espñol" or l_election == "Espaol" or l_election == "Españl" or l_election == "Españo" or l_election == "pañol" or l_election == "epañol" or l_election == "esañol" or l_election == "espñol" or l_election == "espaol" or l_election == "españl" or l_election == "españo"):
        return 1
    elif(l_election == "English" or l_election == "english" or l_election == "0" or l_election == "Eglish" or l_election == "Enlish" or l_election == "Engish" or l_election == "Englsh" or l_election == "Englih" or l_election == "Englis" or l_election == "nglish" or l_election == "eglish" or l_election == "enlish" or l_election == "engish" or l_election == "englsh" or l_election == "englih" or l_election == "englis"):
        return 0
    elif(l_election == "Catala" or l_election == "catala" or l_election == "Català" or l_election == "català" or l_election == "2" or l_election == "Ctala" or l_election == "Caala" or l_election == "Catla" or l_election == "Cataa" or l_election == "Catal" or l_election == "Ctalà" or l_election == "Caalà" or l_election == "Catlà" or l_election == "Cataà" or l_election == "ctala" or l_election == "caala" or l_election == "catla" or l_election == "cataa" or l_election == "catal" or l_election == "ctalà" or l_election == "caalà" or l_election == "catlà" or l_election == "cataà"):
        return 2
    else:
        print("Language not yet avaiable, you can choose english, español or catalan.")
        language_choice()
    print("")

#welcome + notes
def welcome(language):
    if language == 0:
        print("Hello, I'm your mental calculation trainer.")
        print("If you want to stop at any moment, type 'q' and press enter.")
        print("If you have any problems or you want to comment or suggest something, contact me at 'joanalnu5@gmail.com', thank you.")
    elif language == 1:
        print("Hola, soy tu entrenador de cálculo mental.")
        print("Si en algún momento quieres parar, teclea 'q' y presiona enter.")
        print("Si tienes algún problema o quieres hacer una sugerencia o comentario, contáctame en 'joanalnu5@gmail.com', gracias.")
    elif language == 2:
        print("Hola, soc el teu entrenador de càlcul mental.")
        print("Si en algun moment vols parar, tecleja 'q' i pressiona enter.")
        print("Si tens cap problema o vols fer una suggerencia o comentari, contacta'm a 'joanalnu5@gmail.com', gràcies.")
    else:
        i_problem(language)
    print("")

#goodbye
def goodbye(language, puntos, positive_points, negative_points):
    if language == 0:
        print("The game has ended, I hope you have enjoyed it!")
        print("This is your punctuation: ",puntos,". With a total of ",positive_points," correct answers and ",negative_points," incorrects answers.", sep="")
        print("Thank you for playing!!")
    elif language == 1:
        print("El juego se ha acabado. ¡¡Espero que te lo hayas pasado muy bien!!")
        print("Esta es tu puntuación: ",puntos,". Con un total de ",positive_points," respuestas correctas y ",negative_points," respuestas incorrectas", sep="")
        print("¡¡Muchas gracias por jugar!!")
    elif language == 2:
        print("El joc s'ha acabat, moltes gràcies per jugar!!")
        print("La teva puntuació ha estat: ",puntos,". Amb un total de ",positive_points," respostes correctes i ",negative_points," respostes incorrectes.", sep="")
        print("Moltes gràcies per jugar!!")
    else:
        i_problem(language)
    sleep(2)

#FUTURE modes election
def modes_election(language):
    if language == 0:
        m_election = input("You can play training (0) mode or game (1) mode: ")
        if(m_election == "0" or m_election == "training" or m_election == "Training" or m_election == "TRAINING" or m_election == "tRAINING" or m_election == "Taining" or m_election == "Trining" or m_election == "Traning" or m_election == "Traiing" or m_election == "Trainng" or m_election == "Trainig" or m_election == "Trainin" or m_election == "taining" or m_election == "trning" or m_election == "traning" or m_election == "traiing" or m_election == "trainng" or m_election == "trainig" or m_election == "raining" or m_election == "RAINING"):
            return 0
        elif(m_election == "1" or m_election == "game" or m_election == "Game" or m_election == "GAME" or m_election == "gAME" or m_election == "Gme" or m_election == "Gae" or m_election == "Gam" or m_election == "gme" or m_election == "gae" or m_election == "gam" or m_election == "ame" or m_election == "AME"):
            return 1
        else:
            i_problem(language)
    elif language == 1:
        m_election = input("Puedes jugar en modo entrenamiento (0) o modo juego (1): ")
        if(m_election == "0"):
            return 0
        elif(m_election == "1"):
            return 1
        else:
            return i_problem(language)
    elif language == 2:
        m_election = input("Pots jugar a mode entrenament (0) o mode joc (1): ")
        if(m_election == "0"):
            return 0
        elif(m_election == "1"):
            return 1
        else:
            i_problem(language)
    else:
        i_problem(language)
    print("")


#type_calc_election (+, -, *) (only symbols are accepted)
def type_calc_election(language):
    if language == 0:
        calc_election = input("What type of calculus do you want to practise: ")
        if calc_election == "+":
            return 0
        elif calc_election == "-":
            return 1
        elif calc_election == "*":
            return 2
        elif calc_election == '/' or calc_election=='÷':
            return 3
        else:
            i_problem(language)
    elif language == 1:
        calc_election = input("¿Qué tipo de càlculo quieres practicar?")
        if calc_election == "+":
            return 0
        elif calc_election == "-":
            return 1
        elif calc_election == "*":
            return 2
        elif calc_election == '/' or calc_election=='÷':
            return 3
        else:
            i_problem(language)
    elif language == 2:
        calc_election = input("Quin tipus de càlcul vols practicar?")
        if calc_election == "+":
            return 0
        elif calc_election == "-":
            return 1
        elif calc_election == "*":
            return 2
        elif calc_election == '/' or calc_election=='÷':
            return 3
        else:
            i_problem(language)
    else:
        i_problem(language)

def low_high_election(language):
    if language == 0:
        plow = int(input("Lowest number: "))
        phigh = int(input("Highest number: "))
        return plow, phigh
    elif language == 1:
        plow = int(input("Número más bajo: "))
        phigh = int(input("Número más alto: "))
        return plow, phigh
    elif language == 2:
        plow = int(input("Número més baix: "))
        phigh = int(input("Número més alt: "))
        return plow, phigh
    else:
        i_problem(language)


def correct_answer(language, puntos):
    c = randint(0, 4)
    if language == 0:
        if(puntos == 1 or puntos == -1):
            if(c==0):
                print("Correct!! You have ", puntos, " point", sep="")
            elif(c==1):
                print("Very good!! You have ", puntos, " point", sep="")
            elif(c==2):
                print("Excellent!! You have ", puntos, " point", sep="")
            elif(c==3):
                print("Perfect!! You have ", puntos, " point", sep="")
            elif(c==4):
                print("Amazing!! You have ", puntos, " point", sep="")
            else:
                i_problem(language)
        elif(puntos < -1 or puntos > 1 or puntos == 0):
            if(c==0):
                print("Correct!! You have ", puntos, " points", sep="")
            elif(c==1):
                print("Very good!! You have ", puntos, " points", sep="")
            elif(c==2):
                print("Excellent!! You have ", puntos, " points", sep="")
            elif(c==3):
                print("Perfect!! You have ", puntos, " points", sep="")
            elif(c==4):
                print("Amazing!! You have ", puntos, " points", sep="")
            else:
                i_problem(language)
    elif language == 1:
        if(puntos == 1 or puntos == -1):
            if(c==0):
                print("¡¡Correcto!!  Tienes ", puntos, " punto", sep="")
            elif(c==1):
                print("¡¡Muy bien!!  Tienes ", puntos, " punto", sep="")
            elif(c==2):
                print("¡¡Excelente!!  Tienes ", puntos, " punto", sep="")
            elif(c==3):
                print("¡¡Perfecto!!  Tienes ", puntos, " punto", sep="")
            elif(c==4):
                print("¡¡Espectacular!!  Tienes ", puntos, " punto", sep="")
            else:
                i_problem(language)
        elif(puntos <-1 or puntos > 1 or puntos == 0):
            if(c==0):
                print("¡¡Correcto!!  Tienes ", puntos, " puntos", sep="")
            elif(c==1):
                print("¡¡Muy bien!!  Tienes ", puntos, " puntos", sep="")
            elif(c==2):
                print("¡¡Excelente!!  Tienes ", puntos, " puntos", sep="")
            elif(c==3):
                print("¡¡Perfecto!!  Tienes ", puntos, " puntos", sep="")
            elif(c==4):
                print("¡¡Espectacular!!  Tienes ", puntos, " puntos", sep="")
            else:
                i_problem(language)
    elif language == 2:
        if(puntos == 1 or puntos == -1):
            if(c==0):
                print("Correcte!!  Tens ", puntos, " punt", sep="")
            elif(c==1):
                print("Molt bé!!  Tens ", puntos, " punt", sep="")
            elif(c==2):
                print("Excel·lent!!  Tens ", puntos, " punt", sep="")
            elif(c==3):
                print("Perfecte!!  Tens ", puntos, " punt", sep="")
            elif(c==4):
                print("Espectacular!!  Tens ", puntos, " punt", sep="")
            else:
                i_problem(language)
        elif(puntos <-1 or puntos > 1 or puntos == 0):
            if(c==0):
                print("Correcte!!  Tens ", puntos, " punts", sep="")
            elif(c==1):
                print("Molt bé!!  Tens ", puntos, " punts", sep="")
            elif(c==2):
                print("Excel·lent!!  Tens ", puntos, " punts", sep="")
            elif(c==3):
                print("Perfecte!!  Tens ", puntos, " punts", sep="")
            elif(c==4):
                print("Espectacular!!  Tens ", puntos, " punts", sep="")
            else:
                i_problem(language)
    else:
        i_problem(language)


def incorrect_answer(language, puntos):
    if language == 0:
        if(puntos == 1 or puntos == -1):
            print("Oh no, incorrect!! You have ", puntos, " point", sep="")
        elif(puntos < -1 or puntos > 1 or puntos == 0):
            print("Oh no, incorrect!! You have ", puntos, " points", sep="")
    elif language == 1:
        if(puntos == 1 or puntos == -1):
            print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " punto", sep="")
        elif(puntos < -1 or puntos > 1 or puntos == 0):
            print("¡¡Oh no, incorrecto!!  Tienes ", puntos, " puntos", sep="")
    elif language == 2:
        if(puntos == 1 or puntos == -1):
            print("Oh no, incorrecte!! Tens ", puntos, " punt", sep="")
        elif(puntos < -1 or puntos > 1 or puntos == 0):
            print("Oh no, incorrecte!! Tens", puntos, " punts", sep="")
    else:
        i_problem(language)



#training_setup
def training_setup(language):
    low, high = low_high_election(language)
    calc = type_calc_election(language)
    puntos = 0
    positive_points = 0
    negative_points = 0
    print("")
    training(language, low, high, calc, puntos, positive_points, negative_points)

#training
def training(language, low, high, calc, puntos, positive_points, negative_points):
    n1 = randint(low, high)
    n2 = randint(low, high)
    if(calc==0):
        print(n1, '+', n2)
        ans = n1+n2
        player_ans = input()
        if(player_ans=='q'):
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if(player_ans==ans):
                puntos = puntos+1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
            else:
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
    elif(calc==1):
        print(n1, '-', n2)
        ans = n1-n2
        player_ans = input()
        if(player_ans=='q'):
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if(player_ans==ans):
                puntos = puntos+1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
            else:
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
    elif(calc==2):
        print(n1, '*', n2)
        ans = n1*n2
        player_ans = input()
        if(player_ans=='q'):
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if(player_ans==ans):
                puntos = puntos+1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
            else:
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                training(language, low, high, calc, puntos, positive_points, negative_points)
    elif(calc==3):
        if (n1/n2)%2 == 0:
            print(n1, '/', n2)
            ans = n1//n2 #integer division
            player_ans = input()
            if(player_ans=='q'):
                goodbye(language, puntos, positive_points, negative_points)
            else:
                player_ans = int(player_ans)
                if(player_ans==ans):
                    puntos = puntos+1
                    positive_points = positive_points+1
                    correct_answer(language, puntos)
                    training(language, low, high, calc, puntos, positive_points, negative_points)
                else:
                    negative_points = negative_points+1
                    incorrect_answer(language, puntos)
                    training(language, low, high, calc, puntos, positive_points, negative_points)
        else:
            training(language, low, high, calc, puntos, positive_points, negative_points)
    else:
        i_problem(language)

#gaming_setup
def gaming_setup(language):
    if language==0:
        print("This is gaming mode, all types of arithmetic operators can appear (+,-,*).")
    elif language==1:
        print("Este es el modo juego, pueden aparecer todas las operacions aritméticas (+,-,*).")
    elif language==2:
        print("Aquest és el mode joc, poden aparèixer totes les operacions aritimètiques (+,-,*).")
    else:
        i_problem(language)
    print("")

    low, high = low_high_election(language)
    puntos = 0
    positive_points = 0
    negative_points = 0
    print("")
    gaming(language,low, high, puntos, positive_points, negative_points)

#gaming
def gaming(language, low, high, puntos, positive_points, negative_points):
    n1 = randint(low, high)
    n2 = randint(low, high)
    calc = randint(0,2)
    if calc==0:
        print(n1,'+',n2)
        ans=n1+n2
        player_ans = input()
        if player_ans == 'q':
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if player_ans == ans:
                puntos = puntos + 1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
            else:
                puntos = puntos - 1
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
    elif calc==1:
        print(n1,'-',n2)
        ans=n1-n2
        player_ans = input()
        if player_ans == 'q':
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if player_ans == ans:
                puntos = puntos + 1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
            else:
                puntos = puntos - 1
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
    elif calc==2:
        print(n1,'*',n2)
        ans=n1*n2
        player_ans = input()
        if player_ans == 'q':
            goodbye(language, puntos, positive_points, negative_points)
        else:
            player_ans = int(player_ans)
            if player_ans == ans:
                puntos = puntos + 1
                positive_points = positive_points + 1
                correct_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
            else:
                puntos = puntos - 1
                negative_points = negative_points + 1
                incorrect_answer(language, puntos)
                gaming(language, low, high, puntos, positive_points, negative_points)
    else:
        i_problem(language)



def main():
    language = language_choice()
    welcome(language)
    mode = modes_election(language)
    if mode == 0:
        training_setup(language)
    elif mode == 1:
        gaming_setup(language)
    else:
        i_problem(language)

main()
