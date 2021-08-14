my_dict = {
        "apple":"red",
        "banana":"yellow",
        "strawberry":"red",
        "grapes":"red"
        }

def get_rev(x):
    rev = {}
    for key in original:
        value = original[key]
        if value not in rev:
            rev[value] = [key]
        else:
            rev.append(value)
    return rev


print(get_rev(my_dict))
