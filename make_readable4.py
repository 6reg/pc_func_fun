def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02}:{:02}:{02}".format(h,m,s)

print(make_readable(2300))
print(make_readable(3602))

