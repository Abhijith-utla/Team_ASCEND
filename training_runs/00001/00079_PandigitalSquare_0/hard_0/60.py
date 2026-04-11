def sat(n: int):
    s = str(n * n)
    for i in "0123456789":
        assert s.count(i) == 1
    return True

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())
