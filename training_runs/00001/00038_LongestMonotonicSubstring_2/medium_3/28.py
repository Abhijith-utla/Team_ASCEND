def sat(x: List[str], length=737):
    return all(x[i] <= x[i + 1] for i in range(length - 1))

def sol():
    return [x for x in range(737)]

if __name__ == "__main__":
    assert sat(sol())
