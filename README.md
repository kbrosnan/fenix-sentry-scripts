
```
export SENTRY_KEY=<find your api key in the sentry dashboard>

rm -rf events
# Three times because it fetches 25000 events per run
./events.py
./events.py
./events.py

-> % ./crashes_per_date_for_dist.py 11570615
2019-06-06      43
2019-06-07      74
2019-06-08      31
2019-06-09      13
2019-06-10      9
2019-06-11      4
2019-06-12      5
```

