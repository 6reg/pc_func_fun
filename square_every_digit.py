"""
This program takes in an integer and returns the result of
squaring each digit

Pseudocode:
    * create emtpy string to hold result
    * loop through input integer
        * add squared result of each position to result string
    * return result string as an int
"""

def get_square(n):
    res = ""
    for i in str(n):
        res += str(int(i)**2)
    return int(res)

print(get_square(919))
