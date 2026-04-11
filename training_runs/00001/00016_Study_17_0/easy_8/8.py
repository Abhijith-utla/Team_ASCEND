def sat(i: int) -> bool:
    return len(str(i)) < len(str(i + 1))

def sol():
    # Assuming i is a positive integer
    i = 1234
    return len(str(i)) < len(str(i + 1))

if __name__ == "__main__":
    assert sat(sol())
