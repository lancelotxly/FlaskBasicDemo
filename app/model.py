from . import db
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User',backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name
    __str__ = __repr__

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return  '<User %r>' % self.name
    __str__ = __repr__