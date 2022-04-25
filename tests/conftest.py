

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


@pytest.fixture()
def clubs_for_tests():
    server.clubs = [
        {
            "name": "club1",
            "email": "club1@clubs.com",
            "points": "15"
        },
        {
            "name": "club2",
            "email": "club2@clubs.com",
            "points": "5"
        },
        {
            "name": "club3",
            "email": "club3@clubs.com",
            "points": "12"
        }
    ]

    return server.clubs


@pytest.fixture()
def competition_for_tests():
    server.competitions = [
        {
            "name": "competition1",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "30"
        },
        {
            "name": "competition2",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "10"
        }

    ]
    return server.competitions


@pytest.fixture()
def club_for_functional_test():
    return {

            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        }


