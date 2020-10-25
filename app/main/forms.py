from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Interview','Interview'),('Product','Product'),('Business','Business')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Post pitch!')
    

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about yourself',validators=[Required()])
    submit = SubmitField('Save')