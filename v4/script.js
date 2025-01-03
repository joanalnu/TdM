let language;
let mode;
let currentCalculation;
let correctAnswer;
let points = 0;
let calc;

import messages from './messages.js';

function startGame() {
    // Ensure a language is selected
    if (!document.getElementById("language").value) {
        return; // Stop if no language is selected
    }

    language = document.getElementById("language").value; // Set selected language
    document.getElementById("language-selection").style.display = "none"; // Hide the language selection
    document.getElementById("welcome").style.display = "block"; // Show the welcome message

    // Update title and footer based on selected language
    updateTitleAndFooter();

    // Clear previous calculations and answers
    document.getElementById("player-answer").value = '';
    document.getElementById("result-message").innerText = '';

    // Set up event listener for player answer
    document.getElementById("player-answer").removeEventListener("keydown", handleEnterPress); // Remove old listener
    document.getElementById("player-answer").addEventListener("keydown", handleEnterPress); // Add new listener

    // Trigger welcome message and modal content
    getWelcomeMessage();
    createModalContent();
}


function updateTitleAndFooter() {

    document.getElementById("main-title").innerHTML = messages.titles[language];
    document.getElementById("footer").innerHTML = messages.footers[language];
}

function handleEnterPress(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent default form submission behavior
        submitAnswer(); // Call the function to submit the player's answer
    }
}

function getWelcomeMessage() {
    document.getElementById("continue-button").innerHTML = messages.continues[language];
    document.getElementById("welcome-message").innerHTML = messages.welcomeMessages[language];
}

function quitWelcomeMessage() {
    document.getElementById("welcome-section").style.display = "none";
    document.getElementById("mode-selection").style.display = "block";
    document.getElementById("mode-selection-title").innerHTML = messages.modeSelectionTitles[language];

    // Set button titles for the modes
    document.getElementById("mode-1-button").innerHTML = messages.modeButtons.mode1[language];
    document.getElementById("mode-2-button").innerHTML = messages.modeButtons.mode2[language];
}

function modeSelection(selectedMode) {
    mode = selectedMode;
    if (mode === 1) {
        document.getElementById("game-area").style.display = "block";
        generateCalculation();
    } else if (mode === 0) {
        // Training Mode
        document.getElementById("calculation-selection").style.display = "block";
        document.getElementById("mode-selection-title").innerHTML = messages.modeSelectionTitles[language];

        // Calculation buttons
        document.getElementById("calc-1-button").innerHTML = messages.calcButtons.calc1[language];
        document.getElementById("calc-2-button").innerHTML = messages.calcButtons.calc2[language];
        document.getElementById("calc-3-button").innerHTML = messages.calcButtons.calc3[language];
        document.getElementById("calc-4-button").innerHTML = messages.calcButtons.calc4[language];
    }
    document.getElementById("mode-selection").style.display = "none";
}

function selectCalculationType(selectedCalc) {
    calc = selectedCalc;
    document.getElementById("calculation-selection").style.display = "none";
    document.getElementById("game-area").style.display = "block";
    generateCalculation();
}

let previousCalculation;

function generateCalculation() {
    let operator;
    if (mode === 0) { // Training Mode
        operator = calc === 0 ? "+" : calc === 1 ? "-" : calc === 2 ? "*" : "/";
    } else { // Gaming Mode
        operator = ['+', '-', '*', '/'][Math.floor(Math.random() * 4)];
    }

    let n1, n2;
    do {
        n1 = Math.floor(Math.random() * 10) + 1;
        n2 = Math.floor(Math.random() * 10) + 1;
        currentCalculation = `${n1} ${operator} ${n2}`;
    } while (currentCalculation === previousCalculation);

    // Handle division to avoid infinite loop
    if (operator === '/') {
        n1 = Math.floor(Math.random() * 10) + 1; // Ensure n1 is a valid number
        n2 = Math.floor(Math.random() * 9) + 1; // Ensure n2 is not zero
        while (n1 % n2 !== 0) { // Ensure n1 is divisible by n2
            n1 = Math.floor(Math.random() * 10) + 1;
            n2 = Math.floor(Math.random() * 9) + 1; // Avoid zero
        }
        currentCalculation = `${n1} ${operator} ${n2}`;
    }

    correctAnswer = eval(currentCalculation); // Not recommended, but safe for simple calculations
    document.getElementById("calculation").innerHTML = currentCalculation;


    document.getElementById("submit-button").innerHTML = messages.submitButton[language];
    document.getElementById("quit-button").innerHTML = messages.quitButton[language];
    document.getElementById("player-answer").placeholder = messages.yourAnswerText[language];

    document.getElementById("calculation-area").style.display = "block";
    previousCalculation = currentCalculation;
}

function submitAnswer() {

    const playerAnswer = parseInt(document.getElementById("player-answer").value);
    if (playerAnswer === correctAnswer) {
        points++;
        document.getElementById("result-message").innerText = messages.correctMessages[language] + points;
    } else {
        document.getElementById("result-message").innerText = messages.incorrectMessages[language] + correctAnswer;
    }
    document.getElementById("player-answer").value = '';
    generateCalculation();
}

function quitGame() {
    // Hide game area and result message
    document.getElementById("game-area").style.display = "none";
    document.getElementById("calculation-area").style.display = "none";
    document.getElementById("result-message").innerText = '';

    // Show goodbye message for 5 seconds before starting a new game
    

    // Display goodbye message
    document.getElementById("goodbye-section").style.display = "block";
    document.getElementById("goodbye-message").innerHTML = messages.goodbyeMessages[language] + points + messages.pointsInDiffLanguages[language];


    document.getElementById("restart").innerHTML = messages.restartButton[language];


    // // Reset all game state variables
    // language = undefined;
    // mode = undefined;
    // currentCalculation = undefined;
    // correctAnswer = undefined;
    // points = 0;
    // calc = undefined;
    // previousCalculation = undefined;

    // // Optionally reset input fields and other UI elements
    // document.getElementById("player-answer").value = '';
    // document.getElementById("mode-selection").style.display = "none";
    // document.getElementById("calculation-selection").style.display = "none";

    // // Reinitialize the event listener for input
    // document.getElementById("player-answer").removeEventListener("keydown", handleEnterPress);
    // document.getElementById("player-answer").addEventListener("keydown", handleEnterPress);
}



// log in modal
function openModal(modalId){
    document.getElementById(modalId).style.display = 'block';
    }

    function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
    }

    // Close modal when clicking outside of modal content
    window.onclick = function(event) {
    const modals = document.getElementsByClassName('modal');
    for (let modal of modals) {
        if (event.target === modal) {
        modal.style.display = 'none';
        }
    }
}

function createModalContent() {
    const modalTitle = {
        "en": "Log In",
        "es": "Iniciar sesión",
        "ca": "Iniciar sessió",
        "de": "Anmelden",
        "fr": "Se connecter",
        "it": "Accedi",
        "pt": "Entrar",
        "zh": "登录",
        "ja": "ログイン",
        "ko": "로그인"
    };
    const modalContent = {
        "en": "Logging in you can avoid having to configure your game each time.",
        "es": "Al iniciar sesión, puede evitar tener que configurar su juego cada vez.",
        "ca": "Al iniciar sessió, pot evitar haver de configurar el seu joc cada vegada.",
        "de": "Wenn Sie sich anmelden, können Sie vermeiden, Ihr Spiel jedes Mal neu zu konfigurieren.",
        "fr": "En vous connectant, vous pouvez éviter de devoir configurer votre jeu à chaque fois.",
        "it": "Accedendo, puoi evitare di dover configurare il tuo gioco ogni volta.",
        "pt": "Ao entrar, você pode evitar ter que configurar seu jogo a cada vez.",
        "zh": "登录后，您可以避免每次都要配置游戏。",
        "ja": "ログインすると、ゲームを毎回設定する必要がなくなります。",
        "ko": "로그인하면 게임을 매번 설정할 필요가 없습니다."
    };
    const notYetModalContent = {
        "en": "We are sorry to inform that this feature is still under development.",
        "es": "Lo sentimos, pero esta función aún está en desarrollo.",
        "ca": "Ens disculpem, però aquesta funció encara està en desenvolupament.",
        "de": "Wir entschuldigen uns, aber diese Funktion ist noch in der Entwicklung.",
        "fr": "Nous sommes désolés de vous informer que cette fonctionnalité est encore en développement.",
        "it": "Ci scusiamo, ma questa funzionalità è ancora in sviluppo.",
        "pt": "Lamento informar que essa funcionalidade ainda está em desenvolvimento.",
        "zh": "我们很抱歉告诉您，这个功能还在开发中。",
        "ja": "ごめんなさいですが、この機能はまだ開発中です。",
        "ko": "죄송하지만, 이 기능은 아직 개발 중입니다."
    };
    document.getElementById("log-in-title").innerHTML = modalTitle[language];
    document.getElementById("log-in-button").innerHTML = modalTitle[language];
    document.getElementById("log-in-content").innerHTML = notYetModalContent[language];
    const text1 = {
        "en": "Username",
        "es": "Nombre de usuario",
        "ca": "Nom d'usuari",
        "de": "Benutzername",
        "fr": "Nom d'utilisateur",
        "it": "Nome utente",
        "pt": "Nome de usuário",
        "zh": "用户名",
        "ja": "ユーザー名",
        "ko": "사용자 이름"
    }
    const text2 = {
        "en": "Password",
        "es": "Contraseña",
        "ca": "Contrasenya",
        "de": "Passwort",
        "fr": "Mot de passe",
        "it": "Password",
        "pt": "Senha",
        "zh": "密码",
        "ja": "パスワード",
        "ko": "비밀번호"
    }
    document.getElementById("username").placeholder = text1[language];
    document.getElementById("password").placeholder = text2[language];
}