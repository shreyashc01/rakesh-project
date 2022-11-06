from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

class CreateUserForm(FlaskForm):
    usr_id = StringField('User ID',
                         id='usr_id',
                         validators=[DataRequired()])
    usr_name = StringField('NAME',
                      id='usr_name',
                      validators=[DataRequired()])
    usr_password = StringField('Password',
                             id='usr_password',
                             validators=[DataRequired()])
    usr_api_key=StringField('API KEY',
                             id='usr_api_key',
                             validators=[DataRequired()])
    usr_api_secret_key = StringField('API SECRET KEY',
                             id='usr_api_secret_key',
                             validators=[DataRequired()])
    usr_totp_key = StringField('TOTP KEY',
                      id='usr_totp_key',
                      validators=[DataRequired()])
    usr_autologin_status=StringField('AUTOLOGIN',
                      id='usr_autologin_status',
                      validators=[DataRequired()])
    