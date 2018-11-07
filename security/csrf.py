from uuid import uuid4

from flask import session


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid4())
    return session['_csrf_token']
