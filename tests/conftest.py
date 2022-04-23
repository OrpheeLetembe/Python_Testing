

import pytest
from flask import template_rendered

import server


@pytest.fixture()
def app():
    app = server.app
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

"""
@pytest.fixture()
def fixture_load_clubs(monkeypatch):

    def clubs_for_test():
        return [
            {
                "name": "club1",
                "email": "john@simplylift.co",
                "points": "15"
            },
            {
                "name": "club2",
                "email": "club3@clubs.com",
                "points": "5"
            },
            {
                "name": "club3",
                "email": "club3@clubs.com",
                "points": "12"
            }
        ]
    monkeypatch.setattr('server.load_clubs', clubs_for_test)


"""


@pytest.fixture()
def clubs_for_tests():

    clubs = [
        {
            "name": "club1",
            "email": "john@simplylift.co",
            "points": "15"
        },
        {
            "name": "club2",
            "email": "club3@clubs.com",
            "points": "5"
        },
        {
            "name": "club3",
            "email": "club3@clubs.com",
            "points": "12"
         }


    ]
    return clubs
