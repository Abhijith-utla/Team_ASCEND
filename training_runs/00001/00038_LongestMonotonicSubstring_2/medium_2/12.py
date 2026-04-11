def sat(x: List[int], length=737):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [2, 3, 5, 6, 8, 10, 11]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
