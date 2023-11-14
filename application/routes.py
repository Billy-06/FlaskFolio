from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from application import app, login_manager
from application.forms import SignInForm, Register, AddUser

with app.app_context():
    from application.models import User, Admin, create_test_data
    from application import db

    # Create the tables if they don't exist already
    if not db.inspect(db.engine).has_table(db.engine, "user"):
        db.create_all()

        create_test_data(db)

@login_manager.unauthorized_handler
def unauthorized():
    """
    This function is called when a user tries to access a page that requires authentication.
    """
    return redirect(url_for('signin'))

@login_manager.user_loader
def load_user(user_id):
    """
    This function is used to load a user from the database.
    """
    current_user = User.get(user_id)
    return current_user

@app.shell_context_processor
def make_shell_context():
    """
    Shell context processor used to automatically import the following when running 'flask shell':
    """
    return {'db': db, 'User': User, 'Admin': Admin}


@app.route('/')
def home():
    """
    Route for the home page.
    """
    return render_template('home.html')

@app.route('/projects')
def projects():
    """
    Route for the projects page.
    """
    return render_template('projects.html')

@app.route('/games')
def games():
    """
    Route for the games page.
    """
    return render_template('games.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Route for the signin page.
    """

    # If it is a GET request, create a new SignInForm
    if request.method == 'GET':
        signInForm = SignInForm()
        
        
        return render_template('signin.html', form=signInForm)
    # if it is a POST request, validate the form and redirect to the home page
    elif request.method == 'POST':

        signInForm = SignInForm(request.form)

        if signInForm.validate():
            login_user(signInForm.user, remember=signInForm.remember.data)
            
            current_user = signInForm.user
            current_user.authenticated = True

            return redirect(url_for('home'))
        else:
            return render_template('signin.html', form=signInForm)



@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route for the register page.
    """

    # If it is a GET request, create a new Register form
    if request.method == 'GET':
        registerForm = Register()
        
        return render_template('register.html', form=registerForm)
    # if it is a POST request, validate the form and redirect to the home page
    elif request.method == 'POST':
            
            registerForm = Register(request.form)
    
            if registerForm.validate():
                return redirect(url_for('home'))
            else:
                return render_template('register.html', form=registerForm)
            
@app.route('/admin')
@login_required
def admin():
    """
    Admin page route.
    """

    # if user is logged in and is an admin, render the admin page
    # if current_user.is_authenticated and current_user.admin_status:
    #     return render_template('admin.html')
    # else:
    #     flash('You are not authorized to view this page')
    return redirect(url_for('home'))

@app.route('/users')
def users():
    """
    Route for the users page.
    """
    users_list = db.session.execute(db.select(User).order_by(User.id)).scalars().all()

    return render_template('users.html', users=users_list)

@app.route('/users/<int:user_id>')
def user(user_id):
    """
    Route for the user page.
    """
    user = db.session.execute(db.select(User).filter(User.id == user_id)).scalars().first()

    return render_template('user.html', user=user)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """
    Route for deleting a user.
    """
    db.session.execute(db.delete(User).where(User.id == user_id))
    db.session.commit()

    return render_template('delete_user.html', user_id=user_id)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """
    Route for editing a user.
    """
    user = db.session.execute(db.select(User).filter(User.id == user_id)).scalars().first()

    return render_template('edit_user.html', user=user)