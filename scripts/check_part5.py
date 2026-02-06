from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    'p5app',
    r'C:\AI_LEELA-Internship\Flask_Basic\part-5\app.py'
).load_module()

app = mod.app

with app.test_client() as c:
    r = c.get('/projects')
    txt = r.get_data(as_text=True)

    print('status:', r.status_code)
    print('projects_page_loaded:', 'My Projects' in txt)
    print('snippet:\n', txt[:600])
