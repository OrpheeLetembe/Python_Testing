

from locust import HttpUser, task, between


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




