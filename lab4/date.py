from datetime import datetime, timedelta

#ex 1
v_now = datetime.now()
five_ago = v_now - timedelta(days=5)
print(v_now.strftime("%Y-%m-%d"))
print(five_ago.strftime("%Y-%m-%d"))

#ex 2
today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print(yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#ex 3
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#ex 4
date2 = datetime(2024, 2, 18)
date1 = datetime(2024, 2, 17)
difference = date2-date1
print(difference.total_seconds())