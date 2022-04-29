# import server
# from tests.conftest import client


# ensure that a club secretary can connect and reserve places
def test_login_and_reserve_places(client, clubs_for_tests, competition_for_tests):

    club = clubs_for_tests[0]
    competition = competition_for_tests[0]

    client.get('/')
    client.post('/showSummary', data={"email": club['email']})
    client.get(f'/book/{competition["name"]}/{club["name"]}')
    places = 2
    points_available = int(club["points"]) - (places * 3)
    competition_places = int(competition['numberOfPlaces']) - places

    response = client.post('/purchasePlaces', data={"club": club["name"], "competition": competition["name"],
                                                    "places": places})

    data = response.data.decode()
    assert response.status_code == 200
    assert f"<h2>Welcome, {club['email']} </h2>" in data
    assert '<a href="/logout">Logout</a>' in data
    assert club['points'] == points_available
    assert competition['numberOfPlaces'] == competition_places
