from flaskapp import create_app, db
from flaskapp.models import User, Student

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Student': Student}