def get_readable(secs):
    return '{:02}:{:02}:{:02}'.format(secs / 3600, secs / 60 % 60, secs % 60)

print(get_readable(3600))
print(get_readable(8833855))
print(get_readable(62))
