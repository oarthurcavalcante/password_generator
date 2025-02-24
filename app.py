from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    nr_letters = int(data['letters'])
    nr_symbols = int(data['symbols'])
    nr_numbers = int(data['numbers'])

    password = []

    for x in range(nr_letters):
        password.append(random.choice(letters))

    for x in range(nr_symbols):
        password.append(random.choice(symbols))

    for x in range(nr_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)
    concat_password = ''.join(password)
    return jsonify({'password': concat_password})

if __name__ == '__main__':
    app.run(debug=True)