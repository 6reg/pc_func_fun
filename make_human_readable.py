"""
This program converts seconds to HH:MM:SS format
"""

def get_human_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

print(get_human_readable(0))
print(get_human_readable(335885))
print(get_human_readable(120))
