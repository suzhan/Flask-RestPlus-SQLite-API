import os
from flask_migrate import Migrate, MigrateCommand
# flask-script 可以执行外部命令
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
# python manage.py db 输出migrate命令
manager.add_command('db', MigrateCommand)


# python manage.py db
@manager.command
def run():
    app.run()


# 环境测试
def test():
    pass


if __name__ == '__main__':
    manager.run()