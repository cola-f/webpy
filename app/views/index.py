from flask import Blueprint, render_template, request

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.form['tc'])
        if request.form['tc'] == 'kcb.oknm.online.pass.popup.sms.cmd.mno.PS02_SmsMno011Cmd':
            return render_template('sms_auth.html')
        elif request.form['tc'] == 'kcb.oknm.online.pass.popup.push.cmd.mno.PS02_PushMno011Cmd':
            return render_template('qr_auth.html')
        else:
            return render_template('qr_auth.html')
    else:
        return "Hello world"
