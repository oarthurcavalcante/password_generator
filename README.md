# Password Generator Web App

A simple web-based password generator built with **Python** and **Flask**. This application allows users to generate secure passwords by specifying the number of letters, symbols, and numbers they want in their password.

---

## Features

- **Customizable Passwords**: Users can specify the number of letters, symbols, and numbers in their password.
- **Secure**: Passwords are generated using Python's `random` module to ensure randomness.
- **User-Friendly Interface**: A clean and intuitive web interface for easy interaction.

---

## Project Structure

```
password-generator/
│
├── app.py                  # Flask backend (server logic)
├── templates/
│   └── index.html          # Frontend HTML file
├── static/
│   ├── styles.css          # CSS for styling the frontend
│   ├── script.js           # JavaScript for handling form submission
│   └── imgs/
│       └── logo.png        # Logo image for the website
├── README.md               # Project documentation (this file)
└── requirements.txt        # Python dependencies
```

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python's package installer (usually comes with Python)

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. **Install Dependencies**:
   - Install Flask using `pip`:
     ```bash
     pip install flask
     ```
   - Alternatively, install all dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   - Start the Flask development server:
     ```bash
     python app.py
     ```
   - The application will be available at `http://127.0.0.1:5000/`.

---

## How to Use

1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the desired number of letters, symbols, and numbers for your password.
3. Click the **Generate Password** button.
4. Your secure password will be displayed on the screen.

---

## Customization

- **Logo**: Replace `static/imgs/logo.png` with your own logo.
- **Styling**: Modify `static/styles.css` to customize the appearance of the web app.
- **Behavior**: Update `static/script.js` to change how the frontend interacts with the backend.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

Enjoy generating secure passwords! 🔒
