from flask import Flask, Blueprint,render_template,request
import time,os,random, string
from pybo.models import User 

from datetime import datetime


bp = Blueprint("test",__name__,url_prefix="/test")

UPLOAD_DIR="pybo/static/upload"

@bp.route("/seoul_tic")
def seoul_tic():

    return render_template("test/seoul_tic.html")

@bp.route("/gdpark")
def gdpark():

    return render_template("test/gd_park.html")

@bp.route("/rollback")
def rollback_name():
    new_name = make_new("hello.jpg")
    return new_name[26:]


@bp.route("/newname/<name>")
def make_new(name):
    letters = string.ascii_lowercase

    rnd_name = [random.choice(letters) for i in range(10)]

    msg = "".join(rnd_name)
    name_ymdhms = datetime.now().strftime("%Y%m%d-%H:%M:%S")


    
    

    return name_ymdhms+"_"+msg+"_"+name
    

def makedir():
    
    
    name_ymd = datetime.now().strftime("%Y%m%d")
    
    new_dir_path = os.path.join(UPLOAD_DIR,name_ymd)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)

    return new_dir_path

@bp.route("/checkid/<id>")
def checkid(id):
    user = request.args.get(id)

    if user == id:
        return 0
    
    return 1

    

@bp.route("/check_id_form")
def check_id():
    return render_template("test/check_id.html")

    

@bp.route("/deco")
def deco():
    
    return "hello"

@bp.route("/say")
def say():
    ls1 = ['a','b','c']
    
    return render_template("test/say.html",ls1 = ls1)

@bp.route("/login")
def login():
    # 확장자가 있으면 파일 확장자가 없으면 폴더입니다. 알았져?
    return render_template("test/login.html")