def sat(l: list):
    return all(i in range(1000) for i in l if i not in range(1000))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
