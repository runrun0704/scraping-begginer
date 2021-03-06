from datetime import datetime, timedelta, timezone

timestamp = 1562889600

tz = timezone(timedelta(), 'UTC')
utc = datetime.fromtimestamp(timestamp, tz)
print(utc)

tz = timezone(timedelta(hours=+9), 'JST')
jst = datetime.fromtimestamp(timestamp, tz)
print(jst)
print(str(jst)[:-9])