"""
Configuration module for ShoppingBot.

This module prompts the user for configuration settings upon import and provides
constants for various settings like URLs, item names, and user credentials sourced 
from environment variables. Default values are provided for all prompted settings.
"""

import os

# Constants
URL = os.getenv("SHOPPINGBOT_URL")
LOGIN_URL = os.getenv("SHOPPINGBOT_LOGIN_URL")
ITEM_NAME = os.getenv("SHOPPINGBOT_PRODUCT")
USERNAME = os.getenv("SHOPPINGBOT_USERNAME")
PASSWORD = os.getenv("SHOPPINGBOT_PASSWORD")
API_KEY = os.getenv("API_KEY")
