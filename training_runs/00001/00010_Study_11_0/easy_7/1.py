def sat(ls: List[str]):
    # If the list is empty, the function returns True
    if len(ls) == 0:
        return True
    else:
        # For each string in the list, if the length of the set of characters is not equal to the length of the string, the function returns False
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return False

def sat(ls: List[str]):
    # If the list is empty, the function returns True
    if len(ls) == 0:
        return True
    else:
        # For each string in the list, if the length of the set of characters is not equal to the length of the string, the function returns False
        return all(len(set(i)) == len(ls[0]) for i in ls)

# Test the function with some input
print(sat(["abc", "def", "ghi"]))  # This should return True
print(sat(["abc", "ab", "ghi"]))  # This should return False

if __name__ == "__main__":
    assert sat(sol())
