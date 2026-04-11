def sat(i: int) -> bool:
    return len(str(i)) < len(str(i + 1))

def sol():
    return sat(10)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
