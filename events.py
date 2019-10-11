#!/usr/bin/env python3


import json
import os.path
import sys
import time

import requests


ENDPOINT = "https://sentry.prod.mozaws.net/api/0"
EVENTS_ENDPOINT = ENDPOINT + "/projects/operations/fenix/events/"
TOKEN = "SENTRY_TOKEN_HERE"
HEADERS = {"Authorization": "Bearer " + TOKEN}
MAX_PER_FILE = 25000


if __name__ == "__main__":

    events = []

    endpoint = EVENTS_ENDPOINT
    if os.path.exists("events/next.url"):
        with open("events/next.url") as fp:
            endpoint = fp.readline().strip()

    r = requests.get(endpoint, headers=HEADERS)
    r.raise_for_status()
    events += r.json()

    while "next" in r.links and r.links["next"]["results"] == "true":
        r = requests.get(r.links["next"]["url"], headers=HEADERS)
        r.raise_for_status()
        events += r.json()
        if len(events) >= MAX_PER_FILE:
            break

    if len(events) > 0:
        with open("events/events.%d.json" % int(time.time()), "w") as fp:
            json.dump(events, fp, ensure_ascii=False, indent=4)
        with open("events/next.url", "w") as fp:
            fp.write(r.links["next"]["url"])

