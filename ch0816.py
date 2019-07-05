import time
gmt = time.gmtime()	#get current Greenwich Mean Time

print('Time is: %02d/%02d/%04d %02d:%02d %02d sec' % (gmt.tm_mon, gmt.tm_mday, gmt.tm_year, gmt.tm_hour, gmt.tm_min, gmt.tm_sec))

print()
print()

print('below is same function and display, but code has mapping keys\n')

print('Time is: %(month)02d/%(day)02d/%(year)04d %(hour)02d:%(min)02d %(sec)02d sec' % {'year':gmt.tm_year, 'month':gmt.tm_mon, 'day':gmt.tm_mday, 'hour':gmt.tm_hour, 'min':gmt.tm_min, 'sec':gmt.tm_sec})

