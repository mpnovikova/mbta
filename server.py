from flask_script import Manager, Server

import config
from app import create_app

app = create_app(config=config.Development)
manager = Manager(app)
manager.add_command("runserver", Server(threaded=True))

if __name__ == "__main__":
    manager.run()
