def sat(stamps):
    return len(stamps) <= 3 and sum(stamps) == 43

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
