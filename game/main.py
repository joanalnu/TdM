from general import begin

if __name__ == "__main__":
    game = begin()
    language = game.start()
    game.welcome(language)
    
    mode = game.mode_selection(language)

    puntos = 0
    positive_points = 0
    negative_points = 0

    low, high = game.low_high_election(language)


    if mode == 0:    
        calc = game.type_calc_election(language)
        from training import training
        training(language, low, high, calc, puntos, positive_points, negative_points)
    
    elif mode == 1:
        messages = {
            0: "This is gaming mode, all types of arithmetic operators can appear (+,-,*).",
            1: "Este es el modo juego, pueden aparecer todas las operacions aritméticas (+,-,*).",
            2: "Aquest és el mode joc, poden aparèixer totes les operacions aritimètiques (+,-,*).",
        }
        print(messages.get(language, "This is gaming mode, all types of arithmetic operators can appear (+,-,*).\n"))
        from gaming import gaming
        gaming(language, low, high, puntos, positive_points, negative_points)