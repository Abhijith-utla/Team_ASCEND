def sat(i: int) -> bool:
    return len(str(i + 1000)) == len(str(i + 10000))

def sol():
    return len(str(1000)) == len(str(10000))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
