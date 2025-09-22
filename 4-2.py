from datetime import datetime, time, timedelta

target_hour = int(input())

today = datetime.today()
current_time = datetime.combine(today, time(0, 0, 0))
end_time = datetime.combine(today, time(target_hour, 59, 59,))

count = 0

while end_time >= current_time:
    hh_mm_ss = current_time.strftime('%H:%M:%S')
    
    if '3' in hh_mm_ss:
        count += 1
        
    current_time += timedelta(seconds=1)

print(count)