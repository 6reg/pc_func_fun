def get_bool(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+1] == string[i+2]:
            return "Three in a row!"
    return False

print(get_bool("aaa"))
print(get_bool("aabbccddaaa"))
print(get_bool("bbccddsseeddgg"))
