def make_readable(seconds):
    h = seconds/60**2 # divide seconds by 3600 to get total hours
    m = (seconds%60**2)/60 # get remainder to get minutes
    s = (seconds%60**2%60)
    return '{:02}:{:02}:{:02}'.format(h,m,s)

print(make_readable(338855))
print(make_readable(4800))
