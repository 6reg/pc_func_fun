def adj_sum(lst):
    res = []
    for num in range(len(lst)-1):
        res.append(lst[num] + lst[num+1])
    return res

print(adj_sum([3,7,2,11]))
