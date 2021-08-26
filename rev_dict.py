def rev(d):
    reved = {}
    for key in d:
        d[key] = reved[d]
        return reved

d = {
        "apple": "red",
        "banana": "yellow",
        "pear": "green",
        "strawberry": "red",
        "mango": "green"
        }

print(rev(d))


