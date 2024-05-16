from flask import Flask, Blueprint, render_template, request, url_for,g,flash #------
from pybo.models import Question
from pybo.forms import QuestionForm
from werkzeug.utils import redirect #---------------
from datetime import datetime #----------------------------
from pybo import db #----------------------------------
from pybo.forms import AnswerForm
import time
from pybo.views.auth_views import required_login


bp = Blueprint("question", __name__, url_prefix="/question")

@required_login
@bp.route("/delete/<int:question_id>",methods=('GET','POST'))
def delete(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash("삭제 권한이 없습니다")
        return redirect(url_for('question.detail',question_id=question_id))
    else:
        db.session.delete(question)
        db.session.commit()
    return redirect(url_for('question.index'))
    
   

          

@required_login
@bp.route("/update/<int:question_id>",methods=('GET','POST'))
def update(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash("수정권한이 없습니다")
        return redirect(url_for('question.detail',question_id=question_id))

    if request.method == "POST":
        form = QuestionForm()

        if form.validate_on_submit():
            form.populate_obj(question)
            question.update_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)
        g.is_update = True

    return render_template("question/question_update_form.html",form=form)
    


@required_login
@bp.route("/create", methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    

    if request.method == 'POST' and form.validate_on_submit():
        subject = form.subject.data # form 태그에서 데이터를 가져오는 방법2
        content = form.content.data # request.form["content"]
        create_date = datetime.now()
        user_id = form.user_id.data
        question = Question(subject=subject, content=content, create_date=create_date
                            ,user_id=user_id)
        db.session.add(question)     
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("question/question_form.html", form=form)

@bp.route("/detail/<int:question_id>")
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get(question_id)
    return render_template("question/question_detail.html", question=question,form=form)

@bp.route("/list")
def index():
    page = request.args.get("page", type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page,per_page=10)
    return render_template("question/question_list.html", question_list =question_list )