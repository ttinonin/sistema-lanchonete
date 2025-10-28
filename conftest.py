import pytest
from application import Application
from models import db

@pytest.fixture()
def app():
    app = Application("test")
    with app.app.app_context():
        db.create_all()
        yield app.app
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def session(app):
    return db.session