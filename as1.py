def get_as(l):
    return [l[i]+l[i+1] for i in range(len(l)-1)]
print(get_as([1,2,3,4,5]))


