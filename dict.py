d = {
        "Serena": "tennis",
        "Lebron": "basketball",
        "Pele": "soccer"
        }

l = ["Serena", "Lebron", "Greg"]

def change_dict(d,l):
    r = []
    for name in l:
        if name in d:
            r.append(d[name])
        else:
            r.append(name)
    return r

print(change_dict(d,l))
