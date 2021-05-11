from application import app, db
from application.models import Army
from flask import render_template, request, redirect, url_for
from application.forms import ArmyForm


@app.route('/')
@app.route('/home')
def home():
    all_army = Army.query.all()
    return render_template('home.html', title = 'Home', all_army = all_army)

@app.route('/add_amry', methods=["GET","POST"])
def add_army():
    form = ArmyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_army = Army(name=form.name.data,
                        faction=form.faction.data,
                        codex=form.codex.data)
            db.session.add(new_army)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title='Creation', form = form)