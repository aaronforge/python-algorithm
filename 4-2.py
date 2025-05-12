from datetime import datetime, timedelta

n = int(input())

from_time = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
to_time = datetime(year=2025, month=1, day=1, hour=n, minute=59, second=59)

now = from_time

result = 0

while now <= to_time:
    if '3' in str(now):
        result += 1
    now += timedelta(seconds=1)

print(result)
