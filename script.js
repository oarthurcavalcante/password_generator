document.getElementById('passwordForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const letters = document.getElementById('letters').value;
    const symbols = document.getElementById('symbols').value;
    const numbers = document.getElementById('numbers').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            letters: letters,
            symbols: symbols,
            numbers: numbers
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('password').textContent = data.password;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});