#!/usr/bin/env python3
"""
Sample python app, doesn't do much.
"""
from datetime import datetime

import sys
import requests


def get_webpage(url):
    """
    uses requests to pull a webpage, return status code integer
    :param url: URL of webpage to get
    :return: int(status_code)
    """
    session = requests.Session()
    try:
        req = session.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        return -1
    return req.status_code


def get_time():
    """
    Gets current time, returns datetime object
    :return: datetime object
    """
    now = datetime.now()
    return now.strftime("%Y-%M-%d [%Z %z]: %c")


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

    return 0

if __name__ == "__main__":
    sys.exit(main())
