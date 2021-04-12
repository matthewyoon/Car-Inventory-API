from flask import Blueprint, render_template

templates = Blueprint('templates',__name__,template_folder='templates_folder')

@templates.route('/signin', methods = ['GET','POST'])
def signin():
    return render_template('signin.html')