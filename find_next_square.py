"""
This program takes in a number and returns the next integral perfect
square after the one passed in as arg
"""

def get_next_square(this_one):
    x = this_one ** 0.5
    return -1 if x % 1 else (x+1)**2

print(get_next_square(8))
print(get_next_square(9))
print(get_next_square(121))
