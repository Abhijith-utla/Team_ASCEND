def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol():
    # the string to be converted to ASCII
    s = "The five boxing wizards jump quickly"
    # replacing all whitespace characters in the string with no space
    s = s.replace(" ", "")
    # returning the list of ASCII values of the string
    return [ord(c) for c in s]

if __name__ == "__main__":
    assert sat(sol())
