def aba(s):
    new = ''
    v = 'aeiouAEIOU'
    for i in s:
        if i in v:
            new += i + "b" + i.lower()
        else:
            new += i
    return new

print(aba("Cats and Dogs"))
