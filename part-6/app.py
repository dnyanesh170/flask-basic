from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {
        "id": 1,
        "title": "Revise Flask Fundamentals",
        "status": "Completed",
        "priority": "High",
        "due_date": "2026-01-10"
    },
    {
        "id": 2,
        "title": "Develop Personal Portfolio Website",
        "status": "In Progress",
        "priority": "High",
        "due_date": "2026-01-18"
    },
    {
        "id": 3,
        "title": "Upload Projects on GitHub",
        "status": "Pending",
        "priority": "Medium",
        "due_date": "2026-01-25"
    },
    {
        "id": 4,
        "title": "Prepare Internship Documentation",
        "status": "Pending",
        "priority": "Low",
        "due_date": "2026-01-30"
    }
]


@app.route("/")
def index():
    return render_template("index.html", tasks=TASKS)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        next_id = max(task["id"] for task in TASKS) + 1 if TASKS else 1

        new_task = {
            "id": next_id,
            "title": request.form.get("title"),
            "status": request.form.get("status", "Pending"),
            "priority": request.form.get("priority", "Medium"),
            "due_date": request.form.get("due_date", "")
        }

        TASKS.append(new_task)
        return redirect(url_for("index"))

    return render_template("add_task.html")


@app.route("/task/<int:id>")
def task(id):
    selected_task = next((t for t in TASKS if t["id"] == id), None)
    if selected_task is None:
        return "Task not found", 404
    return render_template("task.html", task=selected_task)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task_obj = next((t for t in TASKS if t["id"] == id), None)
    if task_obj is None:
        return "Task not found", 404

    if request.method == "POST":
        task_obj["title"] = request.form.get("title")
        task_obj["status"] = request.form.get("status", "Pending")
        task_obj["priority"] = request.form.get("priority", "Medium")
        task_obj["due_date"] = request.form.get("due_date", "")
        return redirect(url_for("index"))

    return render_template("edit.html", task=task_obj)


@app.route("/delete/<int:id>")
def delete(id):
    global TASKS
    TASKS = [t for t in TASKS if t["id"] != id]
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
