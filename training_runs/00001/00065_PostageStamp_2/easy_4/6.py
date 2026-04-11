def sat(stamps):
    return len(stamps) <= 3 and sum(stamps) == 43

def sol():
    return [1, 2, 3, 4]

if __name__ == "__main__":
    assert sat(sol())
