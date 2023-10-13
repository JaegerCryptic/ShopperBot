"""
This module provides the main entry point for the ShoppingBot application.
The main function initializes the ShoppingBot, logs in, attempts to find and buy the desired item,
and then closes the browser.
"""

from features import shoppingbot
from utils import config


def main():
    """Main function to run the ShoppingBot."""
    browser = shoppingbot.setup_browser()
    shoppingbot.login_with_requests()
    shoppingbot.search_item_with_bs4(browser)
    browser.quit()


if __name__ == "__main__":
    main()
