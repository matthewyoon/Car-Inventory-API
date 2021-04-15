from flask import Blueprint, render_template, request, flash, redirect, url_for
from vehicle_inventory.forms import UserLoginForm, UserSigninForm
from vehicle_inventory.models import User, db, check_password_hash

# Imports for flask login
from flask_login import login_user, logout_user, login_required

templates = Blueprint('templates',__name__,template_folder='templates_folder')

@templates.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data
            print(email, password)

            user = User(email, first_name, last_name, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'user-created')

            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form Inputs')

    return render_template('signup.html', form = form)

@templates.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserSigninForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            logged_user = User.query.filter(User.email == email).first() 
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You have successfully logged in: via email/password', 'auth-success')
                return redirect(url_for('site.home'))
            else:
                flash('Your email/password is incorrect', 'auth-failed')
                return redirect(url_for('templates.signin'))
    
    except:
        raise Exception('Invalid Form Data: Please Check Your Form!')
    return render_template('signin.html', form = form)    

@templates.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))