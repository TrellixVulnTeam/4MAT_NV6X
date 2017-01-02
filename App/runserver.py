"""
This script runs the App application using a development server.
"""

from os import environ
from App import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '55555'))
    except ValueError:
        PORT = 55555
    app.run(HOST, PORT)
