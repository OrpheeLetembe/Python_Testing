
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestServer:

    def setup(self):
        service = Service("tests/functional_tests/chromedriver.exe")

        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:5000/")

    def teardown(self):
        self.driver.close()

    def test_login_with_incorrect_email(self):
        club = {
            "name": "Simply Lift",
            "email": "club@clubs.com",
            "points": "13"
        }

        self.driver.find_element(By.NAME, "email").send_keys(club["email"])
        self.driver.find_element(By.ID, "btnLogin").click()

        assert self.driver.find_element(By.TAG_NAME, "li").text == "Sorry, this email cannot be found"

    def test_login_with_correct_email(self, club_for_functional_test):

        club = club_for_functional_test

        self.driver.find_element(By.NAME, "email").send_keys(club["email"])
        self.driver.find_element(By.ID, "btnLogin").click()

        assert self.driver.find_elements(By.TAG_NAME, "a")[0].text == "Logout"
        assert self.driver.find_element(By.TAG_NAME, "h2").text == f"Welcome, {club['email']}"

    def test_clic_on_past_competition(self, club_for_functional_test):
        club = club_for_functional_test

        self.driver.find_element(By.NAME, "email").send_keys(club["email"])
        self.driver.find_element(By.ID, "btnLogin").click()

        self.driver.find_elements(By.LINK_TEXT, 'Book Places')[1].click()
        assert self.driver.find_element(By.TAG_NAME,
                                        "li").text == "message Sorry, this competition has already taken place." \
                                                      " Please choose another one"

    def test_clic_on_open_competition(self, club_for_functional_test):
        club = club_for_functional_test

        self.driver.find_element(By.NAME, "email").send_keys(club["email"])
        self.driver.find_element(By.ID, "btnLogin").click()

        self.driver.find_elements(By.LINK_TEXT, 'Book Places')[0].click()
        self.driver.find_element(By.NAME, 'places').send_keys(2)
        self.driver.find_element(By.ID, "btnBook").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

        assert self.driver.find_element(By.TAG_NAME, "h1").text == "Welcome to the GUDLFT Registration Portal!"











