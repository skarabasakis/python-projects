// Function to generate a random 4-digit number
function generateRandomNumber() {
    return Math.floor(Math.random() * 9000) + 1000;
  }

  // Get a random 4-digit number
  const randomNumber = generateRandomNumber();

  // Update the content of the span with the random number
  document.getElementById('randomNumber').innerText = randomNumber;