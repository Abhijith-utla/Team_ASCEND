def sat(x: List[int]) -> bool:
    if len(x) < 2:
        return False
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(len(x) - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
