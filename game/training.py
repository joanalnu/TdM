from random import randint
from answers import correct_answer, incorrect_answer, goodbye

# training mode
def training(language, low, high, calc, puntos, positive_points, negative_points):
    while True:
        n1 = randint(low, high)
        n2 = randint(low, high)
        if calc == 0:
            print(n1, '+', n2)
            ans = n1 + n2
        elif calc == 1:
            print(n1, '-', n2)
            ans = n1 - n2
        elif calc == 2:
            print(n1, '*', n2)
            ans = n1 * n2
        elif calc == 3:
            if n2 != 0 and (n1 / n2) % 2 == 0:
                print(n1, '/', n2)
                ans = n1 // n2
            else:
                continue  # Skip this iteration if division is not valid

        player_ans = input()
        if player_ans == 'q':
            return goodbye(language, puntos, positive_points, negative_points)
        
        try:
            player_ans = int(player_ans)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        if player_ans == ans:
            puntos += 1
            positive_points += 1
            correct_answer(language, puntos)
        else:
            negative_points += 1
            incorrect_answer(language, puntos)