def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return {i for i in range(1000)}

if __name__ == "__main__":
    assert sat(sol())
