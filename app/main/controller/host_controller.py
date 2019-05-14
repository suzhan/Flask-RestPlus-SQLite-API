from flask import request
from flask_restplus import Resource
from ..util.dto import HostDto
from ..service.host_service import save_new_host, get_all_hosts, get_a_host

from ..util.dto import DriveDto
from ..service.drive_service import save_new_drive, get_all_drive, get_a_drive


api = HostDto.api
_host = HostDto.host

api_d = DriveDto.api
_drive_d = DriveDto.drive


@api.route('/')
class HostList(Resource):
    @api.doc('list all hosts')
    @api.marshal_list_with(_host, envelope='data')
    def get(self):
        return get_all_hosts()

    @api.expect(_host, validate=True)
    @api.response(201, 'Host successfully created.')
    @api.doc('create a host')
    def post(self):
        data = request.json
        return save_new_host(data=data)


@api.route('/<private_ip>')
@api.param('private_id', 'The host private ip address')
@api.response(404, 'Host not found.')
class Host(Resource):
    @api.doc('get a host')
    @api.marshal_with(_host)
    def get(self, private_ip):
        host = get_a_host(private_ip)
        if not Host:
            api.abort(404)
        else:
            return host


@api_d.route('/<os_drive_id>')
@api.param('al_disk_id', 'The host identifier')
@api.response(404, 'drive not found.')
class Drive(Resource):
    @api.doc('get a drive')
    @api.marshal_with(_drive_d)
    def get(self, al_disk_id):
        drive = get_a_drive(al_disk_id)
        if not drive:
            api.abort(404)
        else:
            return drive