from wtforms import Form, StringField, PasswordField, validators, IntegerField, TextAreaField,SelectField

class AddUser(Form):
    role = SelectField(choices=[('admin', 'Admin'), ('judge', 'Judge'),('visitor','Visitor')])
    name = StringField('Username',[validators.Length(min=4, max=80)])
    email =  StringField('Email',[validators.Length(min=8, max=40)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')


class EditUser(Form):
    role = SelectField(choices=[('admin', 'Admin'), ('judge', 'Judge'),('visitor','Visitor')])
    name = StringField('Username',[validators.Length(min=4, max=80)])
    email =  StringField('Email',[validators.Length(min=8, max=40)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')


class LoginAdmin(Form):
    email = StringField('Email', [
        validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired()])

class ContestForm(Form):
    phone = IntegerField('Phone',[validators.Length(min=10,max=13)])
    text =  TextAreaField('Text',[validators.Length(min=18, max=40)])
