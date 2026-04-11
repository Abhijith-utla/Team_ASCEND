def sat(x: List[int], y: List[int]) -> bool:
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(len(x) - 1))

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
