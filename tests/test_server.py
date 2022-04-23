
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

