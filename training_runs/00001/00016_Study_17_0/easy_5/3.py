def sat(i: int) -> bool:
    return len(str(i + 10)) == len(str(i + 100))

def sol():
    return int(str(10000))

if __name__ == "__main__":
    assert sat(sol())
