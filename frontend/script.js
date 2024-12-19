let language;
let mode;
let currentCalculation;
let correctAnswer;
let points = 0;

function startGame() {
    language = document.getElementById("language").value;
    document.getElementById("language-selection").style.display = "none";
    document.getElementById("game-area").style.display = "block";
    document.getElementById("welcome-message").innerText = getWelcomeMessage(language);
}

function getWelcomeMessage(lang) {
    const messages = [
        "Hello, I'm your mental calculation trainer.",
        "Hola, soy tu entrenador de cálculo mental.",
        "Hola, soc el teu entrenador de càlcul mental."
    ];
    return messages[lang];
}

function selectMode(selectedMode) {
    mode = selectedMode;
    if (mode === 0) {
        // Training Mode
        selectCalculationType();
    } else {
        // Gaming Mode
        generateCalculation();
    }
}

function selectCalculationType() {
    // For simplicity, we will just generate a calculation
    generateCalculation();
}

function generateCalculation() {
    const n1 = Math.floor(Math.random() * 10);
    const n2 = Math.floor(Math.random() * 10);
    const operator = ['+', '-', '*'][Math.floor(Math.random() * 3)];
    currentCalculation = `${n1} ${operator} ${n2}`;
    correctAnswer = eval(currentCalculation);
    document.getElementById("calculation").innerText = currentCalculation;
    document.getElementById("calculation-area").style.display = "block";
}

function submitAnswer() {
    const playerAnswer = parseInt(document.getElementById("player-answer").value);
 if (playerAnswer === correctAnswer) {
        points++;
        document.getElementById("result-message").innerText = "Correct! Points: " + points;
    } else {
        document.getElementById("result-message").innerText = "Wrong! The correct answer was: " + correctAnswer;
    }
    document.getElementById("player-answer").value = '';
    generateCalculation();
}

function quitGame() {
    document.getElementById("game-area").style.display = "none";
    document.getElementById("language-selection").style.display = "block";
    points = 0;
    document.getElementById("result-message").innerText = '';
}