def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return [False] * len(li)

if __name__ == "__main__":
    assert sat(sol())
