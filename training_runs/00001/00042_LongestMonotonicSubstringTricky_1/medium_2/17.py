def sat(x: List[int], length=535) -> bool:
    return all(x[i] <= x[i + 1] for i in range(length - 1))

def sol():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

if __name__ == "__main__":
    assert sat(sol())
