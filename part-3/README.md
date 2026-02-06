# Part 3: Jinja2 Variables – Passing Data to Templates

This part focuses on making Flask applications dynamic by sending data from Python to HTML using the Jinja2 templating engine.

## Learning Goals
- Pass variables from Flask routes to HTML templates
- Display values using {{ variable }} syntax
- Apply Jinja2 filters such as upper, lower, and length
- Iterate over lists using {% for %} loops
- Control content using {% if %} conditionals

## Concepts Covered

### Passing Variables from Python to Templates
Flask sends data to templates using the render_template() function.

Python example:
@app.route("/")
def home():
    user_name = "Dnyanesh Rane"
    return render_template("index.html", name=user_name)

HTML example:
<h1>Hello, {{ name }}</h1>

### Using Jinja2 Filters
Filters allow formatting and transforming data directly inside HTML.

Examples:
{{ name | upper }} → DNYANESH RANE
{{ name | lower }} → dnyanesh rane
{{ name | length }} → number of characters
{{ name | title }} → Dnyanesh Rane

### Conditionals in Templates
Conditionals change what is displayed based on data values.

{% if is_enrolled %}
Active Student
{% else %}
Not Enrolled
{% endif %}

### Looping Through Lists
Loops are used to display multiple items dynamically.

{% for skill in skills %}
{{ skill }}
{% endfor %}

### Useful Loop Variables
- loop.index – current iteration (starts from 1)
- loop.index0 – current iteration (starts from 0)
- loop.first – true if first item
- loop.last – true if last item
- loop.length – total number of items

## How to Run
cd part-3
python app.py

Open the browser and visit:
- http://localhost:5000/ → single variable example
- http://localhost:5000/profile → multiple variables with conditionals
- http://localhost:5000/skills → looping through a list
- http://localhost:5000/projects → list of dictionaries
- http://localhost:5000/grades → data-driven table

## Practice Exercises
1. Add more fields such as email or city to the profile page
2. Modify grades data and test pass/fail logic
3. Change styles based on project status or marks

## Completion Checklist
- Variables display correctly on all pages
- Conditionals work as expected
- Loops render full lists
- At least one page is fully data-driven
