def sum_getter(l):
    res = [l[n]+l[n+1] for n in range(len(l)-1)]
    return res
print(sum_getter([1,2,3,4,5]))
