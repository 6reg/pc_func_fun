def adj(l):
    return [l[i] + l[i+1] for i in range(len(l)-1)]
print(adj([1,2,3,4]))
