"""
Sample python app, doesn't do much.
"""

import requests

from datetime import datetime


def get_webpage(url):
    """
    uses requests to pull a webpage, return status code integer
    :param url: URL of webpage to get
    :return: int(status_code)
    """
    s = requests.Session()
    try:
        r = s.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        return -1
    return r.status_code


def get_time():
    """
    Gets current time, returns datetime object
    :return: datetime object
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d [%Z %z]: %c")


def main():
    """
    Main loop
    :return: 0 or 1
    """
    # get webpage
    result = get_webpage('http://www.google.com')
    print("HTTP status code of trying to get webpage: %i" % result)

    # get time
    current_time = get_time()
    print("Current time: %s" % current_time)

if __name__ == "__main__":
    main()
