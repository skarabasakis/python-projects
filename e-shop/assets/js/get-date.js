// Get the current date
const currentDate = new Date();

// Extract day and month from the current date
const day = currentDate.getDate().toString().padStart(2, '0');
const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');

// Update the content of the span with the current date
document.getElementById('date').innerText = `${day}/${month}`;