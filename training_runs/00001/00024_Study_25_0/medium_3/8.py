def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return ''.join(sorted(input()))

# This function first takes input from the user, sorts the characters in the input string and then checks if the sorted string is the same as the reversed string.
# The checker will run: assert sat(sol())
!cat test.py
!python3 test.py

if __name__ == "__main__":
    assert sat(sol())
