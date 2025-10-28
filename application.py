from flask import Flask
from models import db

class Application:
    def __init__(self, enviorment):
        if enviorment == "test":
            self.test()
        else:
            self.prod()
    
    def prod(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lanchonete.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def test(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

    def run(self):
        pass