def get_aba(o):
    new = ''
    v = 'aeiouAEIOU'
    for ch in o:
        if ch in v:
            new += ch + 'b' + ch.lower()
        else:
            new += ch
    return new

print(get_aba('Cats and Dogs'))
