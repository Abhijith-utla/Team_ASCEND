def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1)) if len(x) > 1 else True

def sol():
    return [1, 2, 3, 4, 5] if sat([1, 2, 3, 4, 5]) else [5, 4, 3, 2, 1]

if __name__ == "__main__":
    assert sat(sol())
