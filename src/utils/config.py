"""
Configuration module for ShoppingBot.

This module prompts the user for configuration settings upon import and provides
constants for various settings like URLs, item names, and user credentials sourced 
from environment variables. Default values are provided for all prompted settings.
"""

import os


def get_input_with_default(prompt, default_value):
    """Get input from the user, but return a default value if they just press Enter."""
    value = input(f"{prompt} (default: {default_value}): ")
    return value if value else default_value


def setup_config():
    """Interactive setup for configuration values."""
    url = get_input_with_default("Enter the URL", "https://www.example.com")
    login_url = get_input_with_default(
        "Enter the login URL", "https://www.example.com/login"
    )
    item_name = get_input_with_default(
        "Enter the desired item name", "Desired Item Name"
    )
    return url, login_url, item_name


# Constants
URL, LOGIN_URL, ITEM_NAME = setup_config()
USERNAME = os.getenv("SHOPPINGBOT_USERNAME")
PASSWORD = os.getenv("SHOPPINGBOT_PASSWORD")
API_KEY = os.getenv("API_KEY")
