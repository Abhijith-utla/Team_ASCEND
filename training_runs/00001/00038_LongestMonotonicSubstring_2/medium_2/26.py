def sat(x: List[int], length=737):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [random.randint(-1000, 1000) for _ in range(737)]
    return x

if __name__ == "__main__":
    assert sat(sol())
