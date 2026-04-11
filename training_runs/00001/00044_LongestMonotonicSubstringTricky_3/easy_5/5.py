def sat(x: List[int], y: List[int]) -> bool:
    return all(x[i] <= y[i] for i in range(len(x)))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
