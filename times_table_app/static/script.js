const fetchButton = document.getElementById('fetchButton');
const checkButton = document.getElementById('checkButton');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const number1 = document.getElementById('number1');
const number2 = document.getElementById('number2');
const problemBox = document.querySelector('.problem-box');
const answerReveal = document.getElementById('answerReveal');
const resultMessage = document.getElementById('resultMessage');


// Function to fetch a multiplication problem from the backend
async function fetchRandomNumber() {
    // Show loading spinner
    loadingSpinner.classList.remove('hidden');
    errorMessage.classList.add('hidden');
    resultMessage.classList.add('hidden');

    try {
        // Fetch from the /numbers endpoint
        const response = await fetch('/numbers');
        
        if (!response.ok) {
            throw new Error('Failed to fetch problem');
        }

        const data = await response.json();

        // Hide loading spinner
        loadingSpinner.classList.add('hidden');

        // Update the number display with animation
        number1.textContent = data.n1;
        number2.textContent = data.n2;
        answerReveal.textContent = '?';
        answerReveal.style.color = 'rgba(255, 255, 255, 0.6)';
        problemBox.style.animation = 'none';
        // Trigger reflow to restart animation
        void problemBox.offsetWidth;
        problemBox.style.animation = 'popIn 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55)';

    } catch (error) {
        // Hide loading spinner
        loadingSpinner.classList.add('hidden');

        // Show error message
        errorMessage.classList.remove('hidden');
        console.error('Error fetching problem:', error);
    }
}

async function checkAnswer() {
    errorMessage.classList.add('hidden');

    const n1 = Number(number1.textContent);
    const n2 = Number(number2.textContent);

    if (Number.isNaN(n1) || Number.isNaN(n2)) {
        resultMessage.textContent = 'Get a problem first!';
        resultMessage.classList.remove('hidden', 'correct');
        resultMessage.classList.add('incorrect');
        return;
    }

    try {
        const response = await fetch(`/multiply?n1=${encodeURIComponent(n1)}&n2=${encodeURIComponent(n2)}`);
        if (!response.ok) {
            throw new Error('Failed to check answer');
        }

        const data = await response.json();
        answerReveal.textContent = String(data.product);
        answerReveal.style.color = 'white';
        resultMessage.textContent = 'Answer revealed!';
        resultMessage.classList.remove('hidden', 'incorrect');
        resultMessage.classList.add('correct');
    } catch (error) {
        errorMessage.classList.remove('hidden');
        console.error('Error checking answer:', error);
    }
}

// Add event listeners to buttons
fetchButton.addEventListener('click', fetchRandomNumber);
checkButton.addEventListener('click', checkAnswer);

// Optional: Fetch a number when the page loads
window.addEventListener('load', () => {
    fetchRandomNumber();
});
