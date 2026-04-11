def sat(x: int, y: int) -> bool:
    return x <= y

def sol():
    return None

assert sat(5, 10) == False
assert sat(10, 5) == True

if __name__ == "__main__":
    assert sat(sol())
