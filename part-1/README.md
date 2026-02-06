# Part 1: Hello Flask – Getting Started

This section introduces Flask by building a simple web server and understanding how routing and responses work.

## Learning Objectives
- Create a basic Flask application
- Understand how URL routing works using @app.route()
- Run a local development server
- See how a browser request is handled by Flask

## Core Concepts

Basic Flask Application Structure
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

app.run(debug=True)

Understanding @app.route("/")
- Maps a URL path to a Python function
- / represents the home page
- Example:
  /about → http://localhost:5000/about

Why debug=True is Used
- Automatically reloads the server when files change
- Displays detailed error messages in the browser
- Should only be used during development, not in production

How to Run the Application

cd part-1
python app.py

Expected Output
Running on http://127.0.0.1:5000
Debugger is active

Open the browser and visit
http://localhost:5000

Practice Exercises
1. Change the welcome message returned on the home page
2. Return HTML instead of plain text, for example <h1>Hello Flask</h1>
3. Add a new route like /about and return a different message

Completion Checklist
- Flask server starts without errors
- Home page loads correctly in the browser
- At least one exercise is completed
