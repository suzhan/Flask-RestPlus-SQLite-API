# Flask-RestPlus-SQLite-API


│  file.txt
│  manage.py
│  README.md
│  requirements.txt
│  
│          
├─app
│  │  __init__.py
│  │  
│  ├─main
│  │  │  config.py
│  │  │  flask_dev.db
│  │  │  __init__.py
│  │  │  
│  │  ├─controller
│  │  │  │  device_controller.py
│  │  │  │  host_controller.py
│  │  │  │  user_controller.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │          
│  │  ├─model
│  │  │  │  drive.py
│  │  │  │  host.py
│  │  │  │  user.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │          
│  │  ├─service
│  │  │  │  drive_service.py
│  │  │  │  host_service.py
│  │  │  │  user_service.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │          
│  │  ├─util
│  │  │  │  dto.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─__pycache__
│  │  │          dto.cpython-36.pyc
│  │  │          __init__.cpython-36.pyc
│  │  │          
│  │  └─__pycache__
│  │          config.cpython-36.pyc
│  │          __init__.cpython-36.pyc
│  │          
│  ├─test
│          
│              
├─migrations
│  │  alembic.ini
│  │  env.py
│  │  README
│  │  script.py.mako
│  │  
│  ├─versions
│  │  │  b25287a68039_.py
│  │  │  
│          
├─static
└─templates
