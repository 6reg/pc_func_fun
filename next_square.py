def find_next_square(q):
    x = q**.5
    return -1 if x%1 else (x+1)**2

print(find_next_square(9), 16)
print(find_next_square(10), -1)
print(find_next_square(11), -1)
print(find_next_square(64), 81)
print(find_next_square(81), 100)
