# Part 4: Dynamic Routes in Flask — URL Parameters

## Overview
This part explains how Flask handles dynamic URLs using parameters. Dynamic routing allows URLs to carry values such as usernames, IDs, categories, and search queries, which are then processed inside Python functions.

## Learning Goals
- Create dynamic routes using <variable> syntax
- Use type converters like int, float, and path
- Capture multiple parameters in a single route
- Generate URLs dynamically using url_for()
- Understand real-world routing patterns (users, posts, products, search)

## Core Concepts

### Basic Dynamic Route
@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}!"

Example URLs:
- /user/Alice
- /user/Rahul

### Type Converters
@app.route('/post/<int:post_id>')
@app.route('/price/<float:amount>')
@app.route('/file/<path:filepath>')

Purpose:
- Automatically validates URL values
- Prevents invalid requests

### Multiple Parameters in One Route
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f"{username}'s post #{post_id}"

Example URLs:
- /user/Alice/post/1
- /user/Bob/post/2

### url_for() Function
from flask import url_for

url_for('home')
url_for('user_profile', username='Bob')

In templates:
<a href="{{ url_for('user_profile', username='Alice') }}">Alice</a>

Why use url_for():
- Avoid hardcoded URLs
- Safer navigation
- Automatic updates if routes change

## How to Run
cd part-4
python app.py

## URLs to Test
- http://localhost:5000/
- http://localhost:5000/user/YourName
- http://localhost:5000/post/1
- http://localhost:5000/user/Alice/post/1
- http://localhost:5000/products
- http://localhost:5000/product/1
- http://localhost:5000/category/electronics/product/1
- http://localhost:5000/search/python
- http://localhost:5000/links

## Exercises
1. Create a product route: /product/<int:id>
2. Add a category route: /category/<name>/product/<int:id>
3. Build a search route: /search/<query>
4. Add a custom 404 error page

## Checklist
- User route works with different names
- Post route accepts only integers
- Multiple parameter routes work correctly
- url_for() generates correct URLs
- Search redirect works as expected

## Summary
In this part, you learned how Flask extracts values from URLs, validates parameters automatically, supports complex routing patterns, and helps you build clean, maintainable web applications using dynamic routes.
