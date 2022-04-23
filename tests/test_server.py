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
            "email": 'club3@clubs.com'
        }

    response = client.post('/showSummary', data={"email": club['email']}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in data
    assert 'Sorry, this email cannot be found' in data


# Ensure that login with good email redirect to index and display message error
def test_login_with_good_email(client):

    club = {
            "email": 'john@simplylift.co'
        }

    response = client.post('/showSummary', data={"email": club['email']})
    data = response.data.decode()
    assert response.status_code == 200
    assert f"<h2>Welcome, {club['email']} </h2>" in data
    assert '<a href="/logout">Logout</a>' in data

