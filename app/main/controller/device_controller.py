from flask import request
from flask_restplus import Resource
from ..util.dto import DriveDto
from ..service.drive_service import save_new_drive, get_all_drive, get_a_drive

api = DriveDto.api
_drive = DriveDto.drive


@api.route('/')
class DriveList(Resource):
    @api.doc('list drive')
    @api.marshal_list_with(_drive, envelope='data')
    def get(self):
        return get_all_drive()

    @api.expect(_drive, validate=True)
    @api.response(201, 'drive successfully created.')
    @api.doc('create a new drive')
    def post(self):
        data = request.json
        return save_new_drive(data=data)


@api.route('/<al_disk_id>')
@api.param('al_disk_id', 'The host identifier')
@api.response(404, 'drive not found.')
class Drive(Resource):
    @api.doc('get a drive')
    @api.marshal_with(_drive)
    def get(self, al_disk_id):
        drive = get_a_drive(al_disk_id)
        if not drive:
            api.abort(404)
        else:
            return drive