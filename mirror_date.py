# unix_time_now
# unix_time_ws
# unix_time_mirror

# mirror = 2 * ws - now

import datetime
import time

# now
unix_time_now = time.time()
print('unix_time_now =', round(unix_time_now))

now_year = datetime.datetime.fromtimestamp(unix_time_now).strftime('%Y')
print('now year =', now_year)


# winter solstice
winter_solstice_year = int(now_year) - 1  # TODO: what if month_now is december?
winter_solstice = '%s-12-22' % winter_solstice_year
datetime_ws = datetime.datetime.strptime(winter_solstice, '%Y-%m-%d')
unix_time_ws = round(time.mktime(datetime_ws.timetuple()))
print('unix_time_ws =', unix_time_ws)

# mirror date
unix_time_mirror = round(2 * unix_time_ws - unix_time_now)
print('unix_time_mirror =', unix_time_mirror)
mirror_date = datetime.datetime.fromtimestamp(unix_time_mirror).strftime('%d. %B')
print('\nthe mirror date is:', mirror_date)
