def sat(i: int) -> bool:
    return len(str(i + 1000)) == len(str(i + 10000))

def sol():
    return sat(0)

# The answer value is a boolean that represents whether the length of the digits in the string representation of (i + 1000) and (i + 10000) are equal. If so, the function will return True, otherwise it will return False.

if __name__ == "__main__":
    assert sat(sol())
