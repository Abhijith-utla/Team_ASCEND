def sat(i: int) -> bool:
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return sat(0)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
