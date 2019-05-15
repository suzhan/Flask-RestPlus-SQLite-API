from .. import db


class Host(db.Model):
    __tablename__ = "host"

    host_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    al_instance_id = db.Column(db.String(255), unique=True, nullable=False)
    cpu = db.Column(db.String(255), nullable=False)
    memory = db.Column(db.String(255), nullable=False)
    private_ip = db.Column(db.String(255), unique=True, nullable=False)
    public_ip = db.Column(db.String(255), nullable=True)
    # os_drive_id = db.Column(db.String(100), unique=True)
    # data_drive_id = db.Column(db.String(100), unique=True)

    drives = db.relationship('Drive', backref=db.backref('host', lazy='dynamic'))

    def __repr__(self):
        return '<Host %r>' % self.name