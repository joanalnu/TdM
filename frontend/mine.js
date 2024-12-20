let language;
let mode;
let currentCalculation;
let correctAnswer;
let points = 0;

function startGame() {
    languages = {
        "English": "en",
        "Spanish": "es",
        "Catalan": "ca",
        "German": "de",
        "French": "fr",
        // "Italian": "it",
        // "Portuguese": "pt",
        // "Chinese": "zh",
        // "Japanese": "ja",
        // "Korean": "ko"  
    };
    language = languages[document.getElementById("laguage").value]; // define language
    document.getElementById("language-selection").style.display = "none"; //quit the language menu
    document.getElementById("game-area").style.display = "block"; // display game UI
    document.getElementById("welcome-message").innnerText = getWelcomeMessage(language);
    document.getElementById("player-answer").addEventListiener("keydown", function(event) { // add enter button
        if (event.key === "Enter") {
            submitAnswer();
        }
    });
}

function getWelcomeMessage(language) {
    const messages = {
        "en": "Hello, I'm your mental calculation trainer.",
        "es": "Hola, soy tu entrenador de cálculo mental.",
        "ca": "Hola, soc el teu entrenador de càlcul mental.",
        "de": "Hallo, ich bin Ihr Trainer für Kopfrechnen.",
        "fr": "Bonjour, je suis votre entraîneur en calcul mental."
    }
    return messages[language];
}

function modeSelection(language) {
    
}