# Part 2: Templates – Rendering HTML Files

This section focuses on serving HTML pages using Flask templates and understanding how backend logic and frontend presentation are kept separate.

## Learning Goals
- Store HTML files inside the templates/ directory
- Use the render_template() function to load HTML pages
- Understand separation of concerns between Python and HTML
- Build multiple pages connected through navigation links

## Concepts Explained

### Why Templates Are Important
In the earlier part, HTML was returned directly from Python code, which becomes difficult to manage as the project grows.

Example of inline HTML:
return "<h1>Hello</h1>"

Using templates keeps code clean and organized:
return render_template("index.html")

The templates Directory
Flask automatically searches for HTML files inside a folder named templates.

### Project structure:
part-2/
├── app.py
└── templates/
    ├── index.html
    ├── about.html
    └── contact.html

### Using render_template()
To render an HTML file, import and use render_template:

from flask import Flask, render_template

@app.route("/")
def home():
    return render_template("index.html")

Flask loads the file from the templates/ folder and sends it to the browser.

### How to Run

cd part-2
python app.py

Open the browser and visit:
http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/contact

### Practice Tasks
1. Update the content of index.html with your own text
2. Improve the layout and information on about.html
3. Create or modify contact.html and link it properly
4. Ensure navigation links work across all pages

## Completion Checklist
- Home, About, and Contact pages load correctly
- Navigation works between all pages
- At least one new or modified template is added
