def sat(x: List[int], length=1):
    return all(x[i] < x[i + 1] for i in range(length))

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
