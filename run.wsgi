import sys
sys.path.insert(0, '/var/www/basic-flask-app')


activate_this = '/var/www/basic-flask-app/venv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from run import app as application
