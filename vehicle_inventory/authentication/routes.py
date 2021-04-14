from flask import Blueprint, render_template, request, flash, redirect, url_for
from vehicle_inventory.forms import UserLoginForm
from vehicle_inventory.models import User, db

templates = Blueprint('templates',__name__,template_folder='templates_folder')

@templates.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(first_name, email, password = password)

            db.session.add(user) #Equivalent to doing an insert statement
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'user-created')

            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form Inputs')

    return render_template('signup.html', form = form)

@templates.route('/signin', methods = ['GET','POST'])
def signin():
    return render_template('signin.html')