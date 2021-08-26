def get_combos(lst):
    res = []
    for i in range(len(lst) - 1):
        d = []
        d.append(lst[i])
        for y in range(i + 1, len(lst) - 1):
           d.append(lst[y])
    if d not in res:
        res.append(d)


    return res

print(get_combos(['a','b','c']))
