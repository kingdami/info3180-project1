from . import db

class UserProfile(db.Model):
    id = db.Column(db.String(50), primary_key=True, unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(80))
    bio = db.Column(db.String(1000))
    dp = db.Column(db.String(100))
    date_created = db.Column(db.String(30))

    def __repr__(self):
        return '<User %r>' % (self.username)
