def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return min(ls) == max(ls) == str(len(ls))

# The last line of the code is the assertion which checks if the function 'sol' returns the correct output.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
