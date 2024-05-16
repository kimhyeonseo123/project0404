from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class QuestionForm(FlaskForm):
    subject = StringField('제목',validators=[DataRequired()])
    content = TextAreaField("내용", validators=[DataRequired()])
    user_id = StringField('작성자',validators=[DataRequired()])
    
class AnswerForm(FlaskForm):
    
    
    content = TextAreaField("내용", validators=[DataRequired()])
    user_id = StringField('작성자',validators=[DataRequired()])
    


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름',validators=[DataRequired(),Length(min=3,max=20)])
    password1 = PasswordField('비밀번호',validators=[DataRequired(), EqualTo('password2','비밀번호가 일치하지 않음')])
    password2 = PasswordField("비밀번호확인",validators=[DataRequired()])
    email = EmailField('이메일확인',validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField("사용자이름",validators=[DataRequired(),Length(min=3,max=20)])
    password = PasswordField('비밀번호',validators=[DataRequired()])
    

    





