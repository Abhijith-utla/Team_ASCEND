def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    return 1001  # Return the number 1001 as the answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
