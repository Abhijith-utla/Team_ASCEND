def sat(i: int) -> bool:
    return len(str(i + 1000)) == len(str(i + 10000))

def sol():
    return 1234

if __name__ == "__main__":
    assert sat(sol())
