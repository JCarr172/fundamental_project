from application import db

class Amry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), )
    complete = db.Column(db.Boolean, default = False)