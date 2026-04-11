def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    return 12345  # This is an example answer object. Replace it with the actual answer.

def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

if __name__ == "__main__":
    assert sat(sol())
