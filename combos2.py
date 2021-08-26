def combos(l):
    res = []
    for i in range(len(l)-1):
        for y in range(i+1, len(l)):
            combo = [l[i], l[y]]
            if combo not in res:
                res.append(combo)
    return res

print(combos([0,1,2,3]))
