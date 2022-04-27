

from locust import HttpUser, task


class ProjectServerTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def list_clubs_point(self):
        self.client.get('/clubsPoints')

    @task(3)
    def login(self):
        self.client.post('/showSummary', {"email": "john@simplylift.co"})

    @task(2)
    def booking(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    @task(2)
    def reserve_place(self):
        self.client.post('/purchasePlaces', {"club": "Simply Lift", "competition": "Spring Festival", "places": 2})

    @task(3)
    def logout(self):
        self.client.get('/logout')
