def aba(s):
    n = ""
    v = "aeiouAEIOU"
    for ch in s:
        if ch in v:
            n += ch + "aba" + ch.lower()
        else:
            n += ch
    return n

print(aba("Cats and Dogs"))
