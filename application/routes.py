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
    return render_template("add_army.html", title='Creation', form = form)

@app.route('/update_army/<number>', methods=['GET','POST'])
def update_army(number):
    form = ArmyForm()
    army = Army.query.filter_by(id = number).first()
    if request.method == 'POST':
        army.name = form.name.data
        army.faction = form.faction.data
        army.codex = form.codex.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_army.html", form=form, title='Update', army=army)

@app.route('/delete/<number>', methods=["GET","POST"])
def delete(number):
    army = Army.query.filter_by(id=number).first()
    db.session.delete(army)
    db.session.commit()
    return redirect(url_for("home"))