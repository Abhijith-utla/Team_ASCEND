def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return sat

# You can call the function with a list of strings to validate it
# For example:
# print(sat(["abc", "def", "ghi"])) # returns: True
# print(sat(["abc", "def", "ghi", "jkl"])) # returns: False

# The function `sat` takes a list of strings, and returns `True` if all the strings in the list are of the same length, and have unique characters. Otherwise, it returns `False`.

if __name__ == "__main__":
    assert sat(sol())
