def sat(li: List[int]) -> bool:
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    def sat(li: List[int]) -> bool:
        return all(j == 3 * i for i, j in enumerate(li))

    return sat

if __name__ == "__main__":
    assert sat(sol())
