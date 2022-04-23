

import pytest
from flask import template_rendered

import server


@pytest.fixture()
def app():
    app = server.app
    app.config.update({"TESTING": True,})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()



