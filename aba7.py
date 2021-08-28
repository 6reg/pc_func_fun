s = "Cats and Dogs"

def aba(s):
    r = ""
    v = "aeiouAEIOU"
    for ch in s:
        if ch in v:
            r += ch + "aba" + ch.lower()
        else:
            r += ch
    return r

print(aba(s))
