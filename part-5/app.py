# ============================================================
# part-5/app.py
# Mini Project – Personal Portfolio Website with Flask
# ============================================================
# How to run:
# 1) (Optional) activate venv
# 2) python app.py
# 3) Open http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
# SITE DATA
# ============================================================

SITE_INFO = {
    "name": "Dnyanesh Rane",
    "title": "MCA Student & Aspiring Software Engineer",
    "bio": (
        "I am a computer science graduate from India with a strong interest in "
        "backend development, problem solving, and building real-world web "
        "applications using Python and Flask. I enjoy learning by building "
        "projects and continuously improving my technical skills."
    ),
    "email": "dnyanesh.rane@example.com",
    "github": "https://github.com/dnyaneshrane",
    "linkedin": "https://www.linkedin.com/in/dnyanesh-rane/",
}

SKILLS = [
    {"name": "Python", "level": 85, "slug": "python"},
    {"name": "HTML & CSS", "level": 78, "slug": "html-css"},
    {"name": "Flask", "level": 70, "slug": "flask"},
    {"name": "JavaScript", "level": 60, "slug": "javascript"},
    {"name": "MySQL & DBMS", "level": 80, "slug": "dbms"},
]

PROJECTS = [
    {
        "id": 1,
        "name": "Personal Portfolio Website",
        "description": (
            "A responsive personal portfolio website built using Flask to "
            "showcase my skills, projects, and learning journey."
        ),
        "tech": ["Python", "Flask", "HTML", "CSS"],
        "status": "Completed",
    },
    {
        "id": 2,
        "name": "Hostel Management System",
        "description": (
            "A web-based system designed for managing hostel admissions, "
            "student records, and room allocations."
        ),
        "tech": ["Python", "Flask", "MySQL", "HTML", "CSS"],
        "status": "Completed",
    },
    {
        "id": 3,
        "name": "Roomie Mart",
        "description": (
            "A Flask-based platform that allows hostel and PG students to "
            "buy and sell second-hand items within their local area."
        ),
        "tech": [
            "Python",
            "Flask",
            "Flask-Login",
            "MySQL",
            "OpenCV",
            "Tesseract OCR",
            "Pillow",
            "NumPy",
            "ReportLab",
        ],
        "features": [
            "User authentication and secure login",
            "Item image upload and validation",
            "OCR-based text extraction from bills",
            "Automatic PDF invoice generation",
            "Database-backed item listings",
        ],
        "status": "In Progress",
    },
]

BLOG_POSTS = [
    {
        "id": 1,
        "title": "Starting My Flask Journey",
        "date": "2025-02-01",
        "content": (
            "Learning Flask helped me clearly understand how backend systems "
            "work. Concepts like routing, templates, and dynamic URLs became "
            "much easier through hands-on practice."
        ),
    },
    {
        "id": 2,
        "title": "Why Projects Matter for MCA Students",
        "date": "2025-02-10",
        "content": (
            "Working on practical projects has significantly improved my "
            "confidence. It bridges the gap between theoretical knowledge "
            "and real industry requirements."
        ),
    },
    {
        "id": 3,
        "title": "Exploring OCR with Python",
        "date": "2025-02-18",
        "content": (
            "Using OpenCV and Tesseract OCR, I experimented with extracting "
            "text from images and generating structured reports automatically."
        ),
    },
]

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    return render_template("index.html", info=SITE_INFO)


@app.route("/about")
def about():
    return render_template(
        "about.html",
        info=SITE_INFO,
        skills=SKILLS
    )


@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        info=SITE_INFO,
        projects=PROJECTS
    )


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    selected_project = next(
        (p for p in PROJECTS if p["id"] == project_id),
        None
    )

    return render_template(
        "project_detail.html",
        info=SITE_INFO,
        project=selected_project,
        project_id=project_id
    )


@app.route("/blog")
def blog():
    return render_template(
        "blog.html",
        info=SITE_INFO,
        posts=BLOG_POSTS
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        info=SITE_INFO
    )


@app.route("/skill/<slug>")
def skill_projects(slug):
    normalized = slug.replace("-", "").lower()

    matched_projects = [
        p for p in PROJECTS
        if any(
            normalized in tech.replace("/", "").lower()
            for tech in p["tech"]
        )
    ]

    readable_skill = slug.replace("-", " ").title()

    return render_template(
        "skill.html",
        info=SITE_INFO,
        skill_name=readable_skill,
        projects=matched_projects
    )


# ============================================================
# APP ENTRY POINT
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)

# ============================================================
# PROJECT STRUCTURE (REFERENCE)
# ============================================================
#
# part-5/
# ├── app.py
# ├── static/
# │   └── style.css
# └── templates/
#     ├── base.html
#     ├── index.html
#     ├── about.html
#     ├── projects.html
#     ├── project_detail.html
#     ├── blog.html
#     ├── contact.html
#     └── skill.html
#
# ============================================================
