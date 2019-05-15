import uuid

from app.main import db
from app.main.model.drive import Drive


def save_new_drive(data):
    drive = Drive.query.filter_by(al_disk_id=data['al_disk_id']).first()
    if not drive:
        new_drive = Drive(
            # drive_id=str(uuid.uuid4()),
            al_disk_id=data['al_disk_id'],
            device=data['device'],
            size=data['size'],
            host_id=data['host_id']
        )
        return save_changes(new_drive)
    else:
        response_object = {
            'status': 'fail',
            'message': 'drive already exists.'
        }
        return response_object, 409


def get_all_drive():
    return Drive.query.all()


def get_a_drive(al_disk_id):
    return Drive.query.filter_by(al_disk_id=al_disk_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()