from flaskapp import app, db
from flaskapp.models import User, Student

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Student': Student}

if __name__ == '__main__':
    app.run