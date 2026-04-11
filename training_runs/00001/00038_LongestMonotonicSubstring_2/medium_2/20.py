def sat(x: List[int], length=737):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [i for i in range(737) if i + 1 < 737]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
