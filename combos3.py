# ['a','b','c']
def get_combos(lst):
    res = []
    for i in range(0, len(lst) -1): # i[0] i[1] i[2]
        for x in range(i+1, len(lst)): # 0+1 = 1, len(lst)=3, 2,3
            z = [lst[i],lst[x]]
            if z not in res:
                res.append(z)
    return res

print(get_combos(["hello", "goodbye", "2", "grease"]))

