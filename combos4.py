def combo(a):
    r = []
    for i in range(0, len(a) - 1): # iterates twice
        for y in range(i+1, len(a)):
            k = [a[i],a[y]]
            if k not in r:
                r.append(k)
    return r

print(combo(["a","b","c","d"]))

