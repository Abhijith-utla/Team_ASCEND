def sat(x: List[str]):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

def sol():
    return [None]

if __name__ == "__main__":
    assert sat(sol())
