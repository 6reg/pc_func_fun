"""
given a list of elements, return a new list with all possible combinations
of the original list of elements
"""
l = ["a","b","c","d"]

def get_combos(l):
    r = []
    for i in range(len(l)-1):
        for y in range(i+1, len(l)):
            h = [l[i],l[y]]
            if h not in r:
                r.append(h)
    return r

print(get_combos(l))
