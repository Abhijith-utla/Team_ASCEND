def sat(li: List[int]) -> bool:
    return all(i == 3 * j for j, i in enumerate(li))

def sol():
    def sat(li: List[int]) -> bool:
        return all(i == 3 * j for j, i in enumerate(li))
    return sat

if __name__ == "__main__":
    assert sat(sol())
