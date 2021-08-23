def aba(s):
    res = ''
    v = 'aeiouAEIOU'
    for i in s:
        if i in v:
            res += i + "b" + i.lower()
        else:
            res += i
    return res

print(aba("Cats and Dogs"))
