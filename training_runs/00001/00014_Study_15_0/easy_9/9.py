def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

def sol():
    def sat(li: List[int]):
        return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

    return sat([1, 2, 3, 6])

if __name__ == "__main__":
    assert sat(sol())
