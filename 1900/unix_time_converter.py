
unix = int(input('Enter a Unix time: '))

days = unix // 86400
hours = (unix - (days * 86400)) // 3600
minutes = ((unix - (days * 86400) - (hours * 3600))) // 60
seconds = ((unix - (days * 86400) - (hours * 3600) - (minutes * 60))) 

print('That is ')
print(days, 'day(s)')
print(hours, 'hour(s)')
print(minutes, 'minute(s)')
print(seconds, 'second(s)')
print('since midnight on January 1, 1970.')