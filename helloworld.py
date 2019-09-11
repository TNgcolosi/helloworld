from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

####  Notes ####
# type 'python' in windows terminal to check that it is working and to activate it
# to create virtual environment directory in your app, be in the right dir and in shell type 'python -m venv venv'
# to activate the virtual environment so that you can use it - 'venv\scripts\activate'
# if you still need to install flask then now 'pip install flask' otherwise skip this step if it is already installed
# to confirm that your virtual environment has pip installed - start the python interpreter and 'import flask'
#  *** to run app***
# import flask '(venv) $ set FLASK_APP=microblog.py(nameofyourapplication.py)'
# (venv) $ flask run