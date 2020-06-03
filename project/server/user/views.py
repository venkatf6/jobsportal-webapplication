from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required

from project.server import bcrypt, db
from project.server.models import User,Profile
from project.server.user.forms import LoginForm, RegisterForm, ProfileForm


user_blueprint = Blueprint('user', __name__,)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash('Thank you for registering.', 'success')
        return redirect(url_for("user.profile"))

    return render_template('user/register.html', form=form)


#email, phonenumber, zipcode, skillset, notifications, created_on
@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(request.form)
    if form.validate_on_submit():
        profile = Profile(
            email=form.email.data,
            phonenumber=form.phonenumber.data,
            zipcode=form.zipcode.data,
            skillset=form.skillset.data,
            notifications=str(form.notifications.data)
        )
        print(profile)
        db.session.add(profile)
        db.session.commit()

        #login_user(user)

        flash('Thank you for creating the profile', 'success')
        #return redirect(url_for('user.profileview',p=profile, _method='POST'))
        #url_for('viewproj', proj=project.project_name, method='GET')
        return render_template('user/profile.html', title='Profile Builder',form=form)
    return render_template('user/profile.html', title='Profile Builder',form=form)



@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('user.profile'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', title='Please Login', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out', 'success')
    return redirect(url_for('main.home'))


@user_blueprint.route('/members')
@login_required
def members():
    return render_template('user/members.html')

@user_blueprint.route('/profileviews/<p>')
@login_required
def profileviews(p):
    import requests
    profile = Profile.query.filter_by(email=p).first()
    #flash("Profile Phone:"+profile.phonenumber+" "+"Profile Email:"+profile.email, 'success')
    flash("Profile Skillset:"+profile.skillset, 'info')

    jcompany = requests.get('https://authenticjobs.com/api/?api_key=33f531e5a92d456447721616bc42d85f&method=aj.jobs.getCompanies&format=Json')
    jcompanies =jcompany.json()
    #flash(jcompanies,'info')
    profile.jcompanies = jcompanies['companies']['company']

    jcategories = requests.get('https://authenticjobs.com/api/?api_key=33f531e5a92d456447721616bc42d85f&method=aj.categories.getlist&format=Json')
    jcat =jcategories.json()
    #flash(jc,'info')
    profile.jcat = jcat

    jcompananytypes = requests.get('https://authenticjobs.com/api/?api_key=33f531e5a92d456447721616bc42d85f&method=aj.company_types.getList&format=Json')
    jcomp =jcompananytypes.json()
    #flash(jc,'info')
    profile.jcomp = jcomp

    jlocations = requests.get('https://authenticjobs.com/api/?api_key=33f531e5a92d456447721616bc42d85f&method=aj.jobs.getLocations&format=Json')
    #flash(jlocations.text,'info')
    profile.jlocations = jlocations.json()   
 
    jsterm = 'https://authenticjobs.com/api/?api_key=33f531e5a92d456447721616bc42d85f&method=aj.jobs.search&keywords='+str(profile.skillset)+'&perpage=50&format=Json'
    #flash(jsterm,'info')
    jsear = requests.get(jsterm)
    jsearch = jsear.json()
    profile.jsearch = jsearch['listings']['listing']
    #flash(profile.jsearch,'info')

    #return render_template('user/profileview.html')
    return render_template('user/profileview.html',profile=profile)

@user_blueprint.route('/profileview/')
@login_required
def profileview():
    flash('Profile View', 'success')
    #return render_template('user/profileview.html')
    return render_template('user/profileview.html', title='Profile Visualizer',profile=profile)



