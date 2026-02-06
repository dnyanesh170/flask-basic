# scripts/test_render_part3.py

from jinja2 import Environment, FileSystemLoader, StrictUndefined
import sys

# Configure Jinja2 environment to load Part 3 templates
env = Environment(
    loader=FileSystemLoader('part-3/templates'),
    undefined=StrictUndefined
)

# Load the template to test
tpl = env.get_template('projects.html')

try:
    # Try rendering with sample data
    tpl.render(
        projects=[
            {
                'name': 'Personal Website',
                'status': 'Completed',
                'tech': 'HTML/CSS'
            }
        ]
    )
    print('Rendered OK')
except Exception as e:
    print('ERR', e)
    sys.exit(1)
