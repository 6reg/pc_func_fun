def combos(l):
    res = []
    for i in range(len(l)-1):
        for y in range(i+1, len(l)):
            mini_lst = [l[i], l[y]]
            if mini_lst not in res:
                res.append(mini_lst)
    return res

print(combos(['a','b','c']))
