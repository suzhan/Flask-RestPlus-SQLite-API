from .. import db


class Host(db.Model):
    __tablename__ = "host"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    al_instance_id = db.Column(db.String(255), unique=True, nullable=False)
    cpu = db.Column(db.String(255), nullable=False)
    memory = db.Column(db.String(255), nullable=False)
    private_ip = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    public_ip = db.Column(db.String(255), nullable=True)

    drive = db.relationship('Drive', backref=db.backref('hosts', lazy='joined'), lazy='dynamic')

    # def __repr__(self):
    #     #     return "<Host '{}'>".format(self.private_ip)