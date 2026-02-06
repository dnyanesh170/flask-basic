# Part 5: Mini Project – Personal Website

## 🎯 Learning Goals
- Combine all Flask concepts into one complete project
- Use template inheritance with a base template
- Serve static files such as CSS
- Build a multi-page website with navigation
- Create a personalized portfolio website

## 📖 New Concepts

### Template Inheritance
Instead of repeating the same navbar and footer on every page, we use a base template.

Base template example:
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav>Navigation Bar</nav>

    {% block content %}
    {% endblock %}

    <footer>Footer Section</footer>
</body>
</html>

Child template example:
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Welcome to My Website</h1>
{% endblock %}

This approach keeps the project clean, reusable, and easy to maintain.

### Static Files (CSS, Images, JS)
Flask serves static files from the static folder.

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

## 📂 Project Structure
part-5/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── projects.html
    ├── project_detail.html
    ├── blog.html
    └── contact.html

## 🚀 How to Run
cd part-5
python app.py

Then open your browser:
http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/projects
http://localhost:5000/project/1
http://localhost:5000/contact

## ✏️ Exercises
1. Personalize the site by editing PERSONAL_INFO, SKILLS, and PROJECTS in app.py
2. Add a blog page using a /blog route
3. Modify static/style.css with your own design
4. Add images to the static folder and use them in templates

## ✅ Final Checklist
- Home page loads correctly
- Navigation works on all pages
- CSS styles are applied
- Dynamic project pages work
- Website is personalized
- Ready for submission

## 📤 Submission Requirements
1. Screenshot of terminal showing Flask server running with (venv)
2. Screenshot of browser showing the website
3. Screenshot of app.py showing route definitions

Caption:
Successfully launched my first Python server! My personal website is now running using Flask.
