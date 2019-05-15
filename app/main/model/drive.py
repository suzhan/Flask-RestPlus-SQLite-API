from .. import db


class Drive(db.Model):
    __tablename__ = "drive"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    al_disk_id = db.Column(db.String(100), unique=True)
    device = db.Column(db.String(100))
    size = db.Column(db.String(100))

    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))
    host = db.relationship('Host', backref=db.backref('drives', lazy='joined'))

    def __repr__(self):
        return '<Drive %r>' % self.al_disk_id
