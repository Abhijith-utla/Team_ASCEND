def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    # Assuming the list ls[1234] and ls[1235] are already defined
    # and have the same length and are valid for the problem statement
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

if __name__ == "__main__":
    assert sat(sol())
