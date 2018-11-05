from flask import render_template, session, url_for, redirect
from .. import db
from ..model import User
from . import  main
from .forms import NameForm

@main.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    form = NameForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username = form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form = form, name = session.get('name'), know = session.get('know'))