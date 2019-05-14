from .. import db


class Drive(db.Model):
    __tablename__ = "drive"

    drive_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_id = db.Column(db.String(100))
    al_disk_id = db.Column(db.String(100), unique=True)
    device = db.Column(db.String(100))
    size = db.Column(db.String(100))
