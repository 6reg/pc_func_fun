def el_rep(l,d):
    res = []
    for element in l:
        if element in d:
            res.append(d[element])
        else:
            res.append(element)
    return res

l = ["Lebron James", "Lionel Messi", "Serena Williams"]
d = {"Serena Willams":"tennis", "LeBron James": "basketball"}

print(el_rep(l,d))
