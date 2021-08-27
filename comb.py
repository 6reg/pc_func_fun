s = ['a','b','c']

def get_cmb(s):
    r = []
    for i in range(len(s)-1):
        for y in range(i+1,len(s)):
            v = [s[i],s[y]]
            if v not in r:
                r.append(v)
    return r

print(get_cmb(s))
