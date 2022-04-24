from flask import render_template

import server
from tests.conftest import client


# Ensure that app was set up correctly
def test_index_page_loads(client):
    response = client.get('/')
    data = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in data
    assert '<a href="/clubsPoints">Display clubs list</a>' in data


# Ensure that club point page loads correctly
def test_display_clubs_points_page(client):
    response = client.get('/clubsPoints')
    data = response.data.decode()
    assert response.status_code == 200
    assert "<title>Summary | GUDLFT Clubs</title>" in data
    assert '<a href="/">Registration</a>' in data


# Ensure that login with wrong email redirect to index and display message error
def test_login_with_wrong_email(client):

    club = {
            "email": '125@club.com'
        }

    response = client.post('/showSummary', data={"email": club['email']}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in data
    assert 'Sorry, this email cannot be found' in data


# ensure that the connection with the correct email address returns to the summary page
def test_login_with_good_email(client, clubs_for_tests):

    club = clubs_for_tests[0]

    response = client.post('/showSummary', data={"email": club['email']})
    data = response.data.decode()
    assert response.status_code == 200
    assert f"<h2>Welcome, {club['email']} </h2>" in data
    assert '<a href="/logout">Logout</a>' in data


# ensure that the user can reserve a place if the competition date has not passed
def test_can_reserve_past_competition(client, clubs_for_tests, competition_for_tests):
    club_test = clubs_for_tests[0]
    competition_test = competition_for_tests[1]

    response = client.get(f'/book/{competition_test["name"]}/{club_test["name"]}')
    data = response.data.decode()
    assert response.status_code == 200
    assert f"<title>Booking for {competition_test['name']} || GUDLFT</title>" in data


# ensure that the user cannot reserve a place if the competition date has passed
def test_cannot_reserve_past_competition(client, clubs_for_tests, competition_for_tests):
    club_test = clubs_for_tests[0]
    competition_test = competition_for_tests[0]

    response = client.get(f'/book/{competition_test["name"]}/{club_test["name"]}')
    data = response.data.decode()
    assert response.status_code == 200
    assert 'Sorry, this competition has already taken place. Please choose another one' in data


# ensure that the number of points used is deducted from the club's balance
def test_update_point(client, clubs_for_tests, competition_for_tests):
    club_test = clubs_for_tests[1]
    competition_test = competition_for_tests[1]
    places = 1
    points_available = int(club_test["points"]) - places
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})

    data = response.data.decode()

    assert response.status_code == 200
    assert 'Great-booking complete!' in data
    assert f'Points available: {points_available}' in data
