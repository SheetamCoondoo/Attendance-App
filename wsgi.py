from app import app

# Gunicorn looks for a module-level WSGI callable.
application = app
