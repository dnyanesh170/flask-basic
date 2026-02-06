"""
Part 1: Hello Flask – First Web Server
=====================================
How to Run:
1. Activate virtual environment
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Dnyanesh! Welcome to your Flask web application."


@app.route("/about")
def about():
    return "This project is created to learn Flask basics and web development."


if __name__ == "__main__":
    app.run(debug=True)


# =============================================================================
# PRACTICE TASKS
# =============================================================================
#
# Task 1: Modify the welcome message with your own text
#
# Task 2: Return HTML instead of plain text
#   Example:
#   return "<h1>Hello Flask</h1><p>Learning web development</p>"
#
# Task 3: Add another route such as /contact
#   Return a short message for the contact page
#
# =============================================================================
