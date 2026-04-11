def sat(x: List[str]) -> bool:
    return all(len(x[i]) <= len(x[i + 1]) and x[i + 1] > x[i] for i in range(len(x) - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
