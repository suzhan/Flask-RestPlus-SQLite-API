from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class HostDto:
    api = Namespace('host', description='host related operations')
    host = api.model('host', {
        'name': fields.String(required=True, description='host name'),
        'al_instance_id': fields.String(description='aliyun instance id'),
        'cpu': fields.String(required=True, description='cpu'),
        'memory': fields.String(required=True, description='memory'),
        'private_ip': fields.String(required=True, description='private ip address'),
        'public_ip': fields.String(description='public ip address'),
        'os_drive_id': fields.String(description='OS Drive Identifier'),
        'data_drive_id': fields.String(description='Data Drive Identifier')
    })


class DriveDto:
    api = Namespace('drive', description='host drive related operations')
    drive = api.model('drive', {
        'al_disk_id': fields.String(required=True, description='aliyun disk id'),
        'device': fields.String(description='disk device name'),
        'size': fields.String(required=True, description='disk size'),
        'host_id': fields.String(description='host Identifier')
    })