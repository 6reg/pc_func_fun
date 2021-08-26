def get_adj_sum(lst):
    new_lst = []
    for i in range(0, len(lst)-1):
        new_lst.append(lst[i] + lst[i+1])
    return new_lst

print(get_adj_sum([3,7,2,11]))
