"""
This program takes in a list and returns a new list
with all possible combinations of the elements in the
first list.
"""

o = [1,2,3,4,5]

def combs(o):
    r = []
    for i in range(0, len(o) - 1):
        for y in range(i+1, len(o)):
            m = [o[i], o[y]]
            if m in r:
                break
            else:
                r.append(m)
    return r

print(combs(o))
print(combs(["a", "b", "c"]))
