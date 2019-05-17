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


def del_a_host(private_ip):
    host = Host.query.filter_by(private_ip=private_ip).first()
    if host:
        return delete_changes(host)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Host not exists.'
        }
        return response_object, 409


def update_a_host(private_ip, data):
    host = Host.query.filter_by(private_ip=private_ip).first()

    if host:
        update_host = Host(
            id=data['id'],
            private_ip=private_ip,
            name=data['name'],
            al_instance_id=data['al_instance_id'],
            cpu=data['cpu'],
            memory=data['memory'],
            public_ip=data['public_ip']
        )
        return update_changes(update_host)


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()


def update_changes(data):
    db.session.merge(data)
    db.session.flush()
    db.session.commit()