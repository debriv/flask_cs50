from flask import   (render_template,
                    url_for, 
                    flash, 
                    redirect, 
                    request , 
                    Blueprint)
from webapp.users.forms import (RegistrationForm)
from webapp.models import User
from webapp import db, bcrypt

users = Blueprint('users',__name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)

        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Please login to continue.', 'success')
        # return redirect(url_for('users.login'))
    return render_template('register.html', title ='Register', form=form)