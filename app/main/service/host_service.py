import uuid

from app.main import db
from app.main.model.host import Host


def save_new_host(data):
    host = Host.query.filter_by(private_ip=data['private_ip']).first()
    if not host:
        new_host = Host(
            name=data['name'],
            al_instance_id=data['al_instance_id'],
            cpu=data['cpu'],
            memory=data['memory'],
            private_ip=data['private_ip'],
            public_ip=data['public_ip']
        )
        return save_changes(new_host)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Host already exists. '
        }
        return response_object, 409


def get_all_hosts():
    return Host.query.all()


def get_a_host(private_ip):
    return Host.query.filter_by(private_ip=private_ip).first()


# def get_a_host_os_drive(os_drive_id):
#     return Drive.query.filter_by(al_disk_id=os_drive_id).first()


# def get_host_drive(host_id):
#     device_test = Drive.query.filter_by(host_id=host_id).first()
#     print(device_test)
#     return device_test


def save_changes(data):
    db.session.add(data)
    db.session.commit()