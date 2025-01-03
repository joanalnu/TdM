import messages from './messages.js';

// Update UI with translated strings
function updateUI() {
    document.getElementById('title').textContent = messages.titles[currentLanguage];
    document.getElementById('footer').innerHTML = messages.footers[currentLanguage];
    document.getElementById('continueButton').textContent = messages.continues[currentLanguage];
    document.getElementById('welcomeMessage').textContent = messages.welcomeMessages[currentLanguage];

    // Update Mode Selection
    document.getElementById('modeSelectionTitle').textContent = messages.modeSelectionTitles[currentLanguage];
    document.getElementById('mode1Button').textContent = messages.modeButtons.mode1[currentLanguage];
    document.getElementById('mode2Button').textContent = messages.modeButtons.mode2[currentLanguage];

    // Update Calculation Buttons
    document.getElementById('calc1Button').textContent = messages.calcButtons.calc1[currentLanguage];
    document.getElementById('calc2Button').textContent = messages.calcButtons.calc2[currentLanguage];
    document.getElementById('calc3Button').textContent = messages.calcButtons.calc3[currentLanguage];
    document.getElementById('calc4Button').textContent = messages.calcButtons.calc4[currentLanguage];

    // Update Submit and Quit buttons
    document.getElementById('submitButton').textContent = messages.submitButton[currentLanguage];
    document.getElementById('quitButton').textContent = messages.quitButton[currentLanguage];

    // Update Answer Messages
    document.getElementById('yourAnswerText').textContent = messages.yourAnswerText[currentLanguage];
}

// Example of a function to handle correct or incorrect answers
function handleAnswer(isCorrect) {
    const answerMessage = isCorrect ? messages.correctMessages[currentLanguage] : messages.incorrectMessages[currentLanguage];
    console.log(answerMessage);
}
