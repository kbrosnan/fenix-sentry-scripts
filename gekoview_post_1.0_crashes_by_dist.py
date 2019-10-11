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

    by_dist = collections.defaultdict(int)
    for event in events:
        dist = int(event["dist"])
        metadata = str(event["metadata"])
        if (dist >= 11721514) and ("NativeCodeCrash" in metadata):
            dist = event["dist"][:10]
            by_dist[dist] += 1

    for k in {k: v for k, v in sorted(by_dist.items(), key=lambda x: x[0])}:
        print("%s\t%d" % (k, by_dist[k]))

