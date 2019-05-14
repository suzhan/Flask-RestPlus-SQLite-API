from flask_restplus import Api
from flask import Blueprint


from .main.controller.user_controller import api as user_ns
from .main.controller.host_controller import api as host_ns
from .main.controller.device_controller import api as device_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask RestPlus API ',
          version='1.0',
          description='Flask RestPlus WEB Service')

api.add_namespace(user_ns, path='/user')
api.add_namespace(host_ns, path='/host')
api.add_namespace(device_ns, path='/drive')