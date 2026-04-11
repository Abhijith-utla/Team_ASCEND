def sat(x: List[int], length=61):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
