l = ["Lebron James", "Lionel Messi", "Serena Williams"]
d = {"Serena Williams": "tennis", "Lebron James": "basketball"}

def get_el(l, d):
    res = []
    for name in l:
        if name in d:
            res.append(d[name])
        else:
            res.append(name)
    return res

print(get_el(l,d))
