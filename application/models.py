from application import db

class Army(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)
    Faction = db.Column(db.String(50), nullable = False)
    Codex = db.Column(db.Integer, nullable = False)
    units = db.relationship('Unit', backref='Army')

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)
    category = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    army_id = db.Column(db.Integer, db.ForeignKey('army.id'), nullable=False)