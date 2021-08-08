def get_phone(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(get_phone([1,1,3,4,5,6,4,3,2,3]))
