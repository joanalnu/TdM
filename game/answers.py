from random import randint

# correct and incorrect answers
def correct_answer(language, puntos):
    messages = {
        0: ["Correct!! You have ", " point", " points"],
        1: ["¡¡Correcto!!  Tienes ", " punto", " puntos"],
        2: ["Correcte!!  Tens ", " punt", " punts"],
    }
    c = randint(0, 4)
    if puntos in [-1, 1]:
        print(messages.get(language, ["Correct!! You have ", " point", " points"])[0], puntos, messages.get(language, ["Correct!! You have ", " point", " points"])[1], sep="")
    else:
        print(messages.get(language, ["Correct!! You have ", " point", " points"])[0], puntos, messages.get(language, ["Correct!! You have ", " point", " points"])[2], sep="")

def incorrect_answer(language, puntos):
    messages = {
        0: "Oh no, incorrect!! You have ",
        1: "¡¡Oh no, incorrecto!!  Tienes ",
        2: "Oh no, incorrecte!! Tens",
    }
    if puntos in [-1, 1]:
        print(messages.get(language, "Oh no, incorrect!! You have ") + str(puntos) + " point", sep="")
    else:
        print(messages.get(language, "Oh no, incorrect!! You have ") + str(puntos) + " points", sep="")

# goodbye
def goodbye(language, puntos, positive_points, negative_points):
    messages = {
        0: f"Thank you for playing! You scored {puntos} points with {positive_points} correct answers and {negative_points} incorrect answers.",
        1: f"¡Gracias por jugar! Has conseguido {puntos} puntos con {positive_points} respuestas correctas y {negative_points} incorrectas.",
        2: f"Gràcies per jugar! Has aconseguit {puntos} punts amb {positive_points} respostes correctes i {negative_points} incorrectes.",
    }
    print(messages.get(language, "Thank you for playing!"))