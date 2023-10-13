import os

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from retry import retry
import requests
from utils import config


# Constants
URL = "https://www.example.com"
LOGIN_URL = "https://www.example.com/login"
ITEM_NAME = "Desired Item Name"
USERNAME = os.getenv("SHOPPINGBOT_USERNAME")
PASSWORD = os.getenv("SHOPPINGBOT_PASSWORD")
API_KEY = os.getenv("API_KEY")


@retry(Exception, tries=3)
def login_with_requests():
    """Login using the requests library."""
    session = requests.Session()
    payload = {"username": config.USERNAME, "password": config.PASSWORD}
    response = session.post(config.LOGIN_URL, data=payload)

    if response.status_code != 200:
        raise Exception("Failed to login")

    return session


def search_item_with_bs4(session):
    """Search for an item using BeautifulSoup."""
    response = session.get(URL + "/search?q=" + ITEM_NAME)
    soup = BeautifulSoup(response.content, "html.parser")
    # Logic to extract item details or availability using BeautifulSoup
    # This will depend on the website's structure


def setup_browser():
    """Setup and return a webdriver instance using webdriver-manager."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return browser


# ... Rest of the Selenium-based functions remain the same
