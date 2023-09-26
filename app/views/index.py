from flask import Blueprint, render_template, request

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template('authentication.html')
    else:
        return "Hello world"
