def make_readable(seconds):
    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours,minutes,seconds)

print(make_readable(338822))
print(make_readable(0))
print(make_readable(3600))
