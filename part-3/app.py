"""
Part 3: Jinja2 Variables – Passing Data from Python to HTML
==========================================================
How to Run:
1. Activate virtual environment
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    student_name = "Dnyanesh Rane"
    return render_template("index.html", name=student_name)


@app.route("/profile")
def profile():
    profile_data = {
        "name": "Dnyanesh Rane",
        "age": 23,
        "course": "Computer Engineering",
        "is_enrolled": True
    }
    return render_template(
        "profile.html",
        name=profile_data["name"],
        age=profile_data["age"],
        course=profile_data["course"],
        is_enrolled=profile_data["is_enrolled"]
    )


@app.route("/skills")
def skills():
    skill_set = [
        "Python",
        "Flask",
        "HTML",
        "CSS",
        "JavaScript",
        "MySQL"
    ]
    return render_template("skills.html", skills=skill_set)


@app.route("/projects")
def projects():
    project_data = [
        {"name": "Student Management System", "status": "Completed", "tech": "Python + Flask"},
        {"name": "Room Rental Platform", "status": "In Progress", "tech": "Web Development"},
        {"name": "Smart Attendance App", "status": "Planned", "tech": "Machine Learning"}
    ]
    return render_template("projects.html", projects=project_data)


@app.route("/grades")
def grades():
    grade_data = [
        {"name": "Mathematics", "marks": 78},
        {"name": "Data Structures", "marks": 65},
        {"name": "Database Systems", "marks": 72},
        {"name": "Operating Systems", "marks": 39},
        {"name": "Computer Networks", "marks": 81}
    ]
    return render_template("grades.html", grades=grade_data)


if __name__ == "__main__":
    app.run(debug=True)


# =============================================================================
# JINJA2 QUICK SYNTAX GUIDE
# =============================================================================
#
# {{ variable }}                 → display variable
# {{ variable | upper }}         → filter example
# {{ variable | length }}        → get length
#
# {% if condition %}             → conditional block
# {% else %}
# {% endif %}
#
# {% for item in list %}         → loop block
# {{ loop.index }}               → current index (1-based)
# {% endfor %}
#
# =============================================================================
#
# This file is fully compatible with:
# templates/index.html
# templates/profile.html
# templates/skills.html
# templates/projects.html
# templates/grades.html
#
# =============================================================================
