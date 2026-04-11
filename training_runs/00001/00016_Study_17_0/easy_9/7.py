def sat(i: int) -> bool:
    return i < (i + 1)

def sol() -> int:
    i = 0
    while sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
