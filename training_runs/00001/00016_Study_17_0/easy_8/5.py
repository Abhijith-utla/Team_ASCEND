def sat(i: int) -> bool:
    return len(str(i)) < len(str(i + 1))

def sol():
    return len(str(10)) < len(str(11))

if __name__ == "__main__":
    assert sat(sol())
