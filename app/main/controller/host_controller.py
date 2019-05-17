from flask import request
from flask_restplus import Resource
from ..util.dto import HostDto
from ..service.host_service import save_new_host, get_all_hosts, get_a_host, del_a_host, update_a_host


api = HostDto.api
_host = HostDto.host


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
@api.param('private_ip', 'The host private ip address')
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

    @api.doc('delete a host')
    @api.marshal_with(_host)
    def delete(self, private_ip):
        host = del_a_host(private_ip)
        if not Host:
            api.abort(404)
        else:
            return host

    @api.doc('update a host')
    # @api.param('private_ip')
    @api.marshal_with(_host)
    @api.expect(_host)
    def put(self, private_ip):
        data = request.json
        return update_a_host(private_ip, data)