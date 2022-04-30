import statsd
statsd_client = statsd.StatsClient('localhost', 8125, prefix='ncirl.pgdcloud.devsecops')
statsd_client.incr('login.attempts')
print("sent.....")
