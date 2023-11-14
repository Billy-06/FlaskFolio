from flask_wtf import FlaskForm
from wtforms import ( StringField, PasswordField, SubmitField, 
                     BooleanField, TextAreaField, SelectField)
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import User

# Create a sign in form class
class SignInForm(FlaskForm):
    """
    Sign in form for existing users
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate(self, extra_validators=None) -> bool:
        """
        This function checks if the user exists and if the password is correct.
        """

        # Check if user exists
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Invalid email or password')
            return False
        # if the user exists verify the password
        if not user.verify_password(self.password.data):
            self.email.errors.append('Invalid email or password')
            return False
        return True


# Create a registration form class
class Register(FlaskForm):
    """
    Registration form for new users
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate(self, extra_validators=None) -> bool:
        """
        This function checks if the user already exists.
        """
        # Check if user exists
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already in use')
            return False
        
        return True

# Create a form for the admin to add a new user
class AddUser(FlaskForm):
    """
    This form is used by the admin to add users to the website
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('user', 'User'), ('admin', 'Admin')])
    submit = SubmitField('Add User')

    def validate(self, extra_validators=None):
        """
        This function checks if the user already exists.
        """
        # Check if user exists
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already in use')
            return False
        
        return True

class CreateBlogPost(FlaskForm):
    """
    This form is used to add blog posts to the website
    """
    title = StringField('Title', validators=[DataRequired(), Length(min=4)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Post')

    