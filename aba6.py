def get_aba(s):
    res = ''
    v = 'aeiouAEIOU'
    for ch in s:
        if ch in v:
            res += ch + 'b' + ch.lower()
        else:
            res += ch
    return res

print(get_aba("Everyone can code"))
