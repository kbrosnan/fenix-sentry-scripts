#!/usr/bin/env python3


import collections
import glob
import json
import sys


def arch(event):
    a = event.get("contexts", {}).get("device", {}).get("arch")
    if a == "armeabi-v7a":
        return 0
    if a == "arm64-v8a":
        return 1
    if a == "x86":
        return 2
    if a == "x86_64":
        return 3


if __name__ == "__main__":

    dist_filter = sys.argv[1]

    events = []
    for path in glob.glob("events/*.json"):
        with open(path) as f:
            events += json.load(f)

    by_date = collections.defaultdict(int)
    for event in events:
        dist = str(int(event["dist"]) - arch(event))
        if dist == dist_filter:
            date = event["dateCreated"][:10]
            by_date[date] += 1

    for k in {k: v for k, v in sorted(by_date.items(), key=lambda x: x[0])}:
        print("%s\t%d" % (k, by_date[k]))

