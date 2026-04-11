def sat(x):
    return all(i <= j for i, j in enumerate(x))

def sol():
    return None

if __name__ == "__main__":
    assert sat(sol())
