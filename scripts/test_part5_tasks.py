# scripts/test_part5_tasks.py

from importlib.machinery import SourceFileLoader

# Load the Part 5 Flask app dynamically
mod = SourceFileLoader(
    'p5app',
    r'C:\AI_LEELA-Internship\Flask_Basic\part-5\app.py'
).load_module()

app = mod.app

with app.test_client() as c:
    # Test GET /tasks
    r = c.get('/tasks')
    print('status', r.status_code)
    txt = r.get_data(as_text=True)
    print(txt[:600])

    # Test POST /tasks/add
    r2 = c.post(
        '/tasks/add',
        data={
            'title': 'Test Task from script',
            'area': 'QA',
            'priority': 'Low',
            'status': 'Planned',
            'description': 'Created by test'
        },
        follow_redirects=True
    )
    print('add status', r2.status_code)
    print('contains new task?', 'Test Task from script' in r2.get_data(as_text=True))
