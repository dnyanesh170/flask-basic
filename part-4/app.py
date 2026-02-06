# FILE: app.py
"""
Part 4: Dynamic Routes - URL Parameters
=======================================
How to Run:
1. Activate virtual environment
2. Run: python app.py
3. Open browser and try:
   /user/YourName
   /post/1
   /product/2
   /search/python
"""

from flask import Flask, render_template, url_for, request, redirect, abort

app = Flask(__name__)


# =========================================================
# BASIC PAGES
# =========================================================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


# =========================================================
# USER ROUTES
# =========================================================
@app.route("/user/<username>")
def user_profile(username):
    return render_template("user.html", username=username)


@app.route("/user/<username>/post/<int:post_id>")
def user_post(username, post_id):
    return render_template("user_post.html", username=username, post_id=post_id)


# =========================================================
# POST ROUTES
# =========================================================
@app.route("/post/<int:post_id>")
def show_post(post_id):
    posts = {
        1: {"title": "Introduction to Flask", "content": "Flask is a lightweight Python web framework."},
        2: {"title": "Routing in Flask", "content": "Routes connect URLs to Python functions."},
        3: {"title": "Templates with Jinja2", "content": "Jinja2 helps render dynamic HTML."}
    }

    post = posts.get(post_id)
    return render_template("post.html", post_id=post_id, post=post)


# =========================================================
# PRODUCT ROUTES
# =========================================================
@app.route("/products")
def products():
    products = {
        1: {"name": "Laptop", "price": 75000},
        2: {"name": "Smartphone", "price": 42000},
        3: {"name": "Tablet", "price": 28000}
    }
    return render_template("products.html", products=products)


@app.route("/product/<int:product_id>")
def product_page(product_id):
    products = {
        1: {"name": "Laptop", "price": 75000},
        2: {"name": "Smartphone", "price": 42000},
        3: {"name": "Tablet", "price": 28000}
    }

    product = products.get(product_id)
    if not product:
        abort(404)

    return render_template("product.html", product_id=product_id, product=product)


@app.route("/category/<category_name>/product/<int:product_id>")
def category_product(category_name, product_id):
    return render_template(
        "category_product.html",
        category=category_name,
        product_id=product_id
    )


# =========================================================
# SEARCH ROUTES
# =========================================================
@app.route("/search/<query>")
def search(query):
    return render_template("search.html", query=query)


@app.route("/search-redirect")
def search_redirect():
    query = request.args.get("q", "").strip()
    if query:
        return redirect(url_for("search", query=query))
    return redirect(url_for("home"))


# =========================================================
# URL BUILDER DEMO
# =========================================================
@app.route("/links")
def show_links():
    links = {
        "home": url_for("home"),
        "about": url_for("about"),
        "user_rahul": url_for("user_profile", username="Rahul"),
        "user_amit": url_for("user_profile", username="Amit"),
        "post_1": url_for("show_post", post_id=1),
        "post_2": url_for("show_post", post_id=2),
        "product_1": url_for("product_page", product_id=1),
        "search_python": url_for("search", query="python flask"),
    }
    return render_template("links.html", links=links)


# =========================================================
# APP ENTRY POINT
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)


# =========================================================
# URL PARAMETER TYPES (REFERENCE)
# =========================================================
# <variable>         -> string (default)
# <int:variable>     -> integer
# <float:variable>   -> float
# <path:variable>    -> string including slashes
# <uuid:variable>    -> UUID
# =========================================================
