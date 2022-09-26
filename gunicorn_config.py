command = '/home/newuser/myapps/portfolio_v2/django-portfolio/venv/bin/gunicorn'
pythonpath = '/home/newuser/myapps/portfolio_v2/django-portfolio'
bind = '127.0.0.1:8001'
workers = 3
user = 'newuser'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=portfolio.settings'
