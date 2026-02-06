"""
Part 2: Templates – Rendering HTML Pages
=======================================
How to Run:
1. Activate the virtual environment
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE
# =============================================================================
#
# part-2/
# ├── app.py
# └── templates/
#     ├── index.html
#     ├── about.html
#     └── contact.html
#
# =============================================================================
#
# PRACTICE TASKS
#
# 1. Edit index.html and update page content
# 2. Modify about.html to add more explanation text
# 3. Update contact.html form layout or fields
# 4. Add navigation links on all pages and test routing
#
# =============================================================================
