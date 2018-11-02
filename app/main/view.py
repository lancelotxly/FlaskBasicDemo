from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..model import User

@main.route('/', methods = ['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #...
        return redirect(url_for('main.index'))
    return  render_template('index.html', name = session.get('name'), know = session.get('Know',False),current_time = datetime.utcnow())
