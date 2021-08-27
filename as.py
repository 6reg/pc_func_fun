
def get_sum(o):
    return [o[n]+ o[n+1] for n in range(0, len(o)-1)]

print(get_sum([1,2,3,4]))
