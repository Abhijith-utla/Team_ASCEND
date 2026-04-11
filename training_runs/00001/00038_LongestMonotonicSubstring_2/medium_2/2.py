def sat(x: List[int], length=737):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [5, 3, 2, 8, 7, 6, 9, 1]

if __name__ == "__main__":
    assert sat(sol())
