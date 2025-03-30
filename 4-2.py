import sys
from datetime import timedelta
input = sys.stdin.readline

n = int(input())
result = 0

cnt = 0
start_time = timedelta(hours=0, minutes=0, seconds=0)
end_time = timedelta(hours=n, minutes=59, seconds=59)

while start_time < end_time:
    if '3' in str(start_time):
        result += 1

    start_time += timedelta(seconds=1)

print(result)
print(cnt)