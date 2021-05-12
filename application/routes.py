from application import app, db
from application.models import Army, Unit
from flask import render_template, request, redirect, url_for
from application.forms import ArmyForm, UnitForm


@app.route('/')
@app.route('/home')
def home():
    all_army = Army.query.all()
    all_unit = Unit.query.all()
    return render_template('home.html', title = 'Home', all_army = all_army, all_unit=all_unit)

@app.route('/view_army/<number>')
def view_army(number):
    army_unit = Unit.query.filter_by(army_id = number)
    army_name = (Army.query.filter_by(id = number).first()).name
    return render_template('view_army.html', title = 'Army view', army_unit=army_unit, army_name=army_name)

@app.route('/add_army', methods=["GET","POST"])
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
    return render_template("add_army.html", title='Add army', form = form)

@app.route('/update_army/<number>', methods=['GET','POST'])
def update_army(number):
    form = ArmyForm()
    army = Army.query.filter_by(id = number).first()
    if request.method == 'POST':
        if form.validate_on_submit():
            army.name = form.name.data
            army.faction = form.faction.data
            army.codex = form.codex.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("update_army.html", form=form, title='Update', army=army)

@app.route('/delete_army/<number>', methods=["GET","POST"])
def delete_army(number):
    army = Army.query.filter_by(id=number).first()
    units = Unit.query.filter_by(army_id=army.id)
    for unit in units:
        db.session.delete(unit)
        db.session.commit()
    db.session.delete(army)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/add_unit', methods=["GET","POST"])
def add_unit():
    form = UnitForm()
    armies = Army.query.all()
    for army in armies:
        form.army.choices.append((army.id, f"{army.name}"))
    if request.method == "POST":
        if form.validate_on_submit():
            new_unit = Unit(name=form.name.data,
                        army_id=form.army.data,
                        category=form.category.data,
                        price=form.price.data,
                        quantity=form.quantity.data)
            db.session.add(new_unit)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add_unit.html", title='Add unit', form = form)