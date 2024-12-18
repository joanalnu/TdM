from time import sleep

class begin():

    def start(self):
        languages = {
            "español": 1,
            "english": 0,
            "catala": 2,
        }
        while True:
            l_election = input("First choose a language | Primero, elige un lenguaje | Primer escull una llengua : ").lower()
            for key in languages:
                if l_election in {key, str(languages[key])}:
                    return languages[key]
            print("Language not yet available, you can choose english (0), español (1) or catalan (2).")

    # welcome + notes
    def welcome(self, language):
        messages = {
            0: "Hello, I'm your mental calculation trainer.",
            1: "Hola, soy tu entrenador de cálculo mental.",
            2: "Hola, soc el teu entrenador de càlcul mental.",
        }
        print(messages.get(language, "Welcome to the mental calculation trainer."))
        print("If you want to stop at any moment, type 'q' and press enter.")
        print("If you have any problems or you want to comment or suggest something, contact me at 'joanalnu5@gmail.com', thank you.")
        print("")
    
    # mode selection
    def mode_selection(self, language):
        messages = {
            0: "You can play training (0) mode or game (1) mode: ",
            1: "Puedes jugar en modo entrenamiento (0) o modo juego (1): ",
            2: "Pots jugar a mode entrenament (0) o mode joc (1): ",
        }
        m_election = input(messages.get(language, "Choose a mode: "))
        if m_election in ["0", "training"]:
            return 0
        elif m_election in ["1", "game"]:
            return 1
        else:
            return i_problem(language)

    def low_high_election(self, language):
        messages = {
            0: ["Lowest number: ", "Highest number: "],
            1: ["Número más bajo: ", "Número más alto: "],
            2: ["Número més baix: ", "Número més alt: "],
        }
        plow = int(input(messages.get(language, ["Lowest number: ", "Highest number: "])[0]))
        phigh = int(input(messages.get(language, ["Lowest number: ", "Highest number: "])[1]))
        return plow, phigh

    def type_calc_election(self, language):
        messages = {
            0: "What type of calculus do you want to practise: ",
            1: "¿Qué tipo de càlculo quieres practicar?",
        2: "Quin tipus de càlcul vols practicar?",
        }
        calc_types = {
            "+": 0,
            "-": 1,
            "*": 2,
            "/": 3,
            "÷": 3,
        }
        while True:
            calc_election = input(messages.get(language, "Choose a calculus type: "))
            if calc_election in calc_types:
                return calc_types[calc_election]
            else:
                return i_problem(language)
