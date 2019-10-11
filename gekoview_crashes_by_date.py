#!/usr/bin/env python3


import collections
import glob
import json
import sys


def arch(event):
    a = event.get("contexts", {}).get("device", {}).get("arch")

if __name__ == "__main__":
    events = []
    for path in glob.glob("events/*.json"):
        with open(path) as f:
            events += json.load(f)

    by_date = collections.defaultdict(int)
    for event in events:
        dist = int(event["dist"])
        metadata = str(event["metadata"])
        if "NativeCodeCrash" in metadata:
            date = event["dateCreated"][:10]
            by_date[date] += 1

    for k in {k: v for k, v in sorted(by_date.items(), key=lambda x: x[0])}:
        print("%s\t%d" % (k, by_date[k]))

