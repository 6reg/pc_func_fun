def get_phone(n):

    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(get_phone([1,2,3,4,5,6,7,8,9,0]))
