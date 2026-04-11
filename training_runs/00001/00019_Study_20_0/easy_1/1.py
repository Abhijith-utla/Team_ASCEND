def sat(li: List[int]):
    # Check if all elements in the list are either 0, 1, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    def sat(li: List[int]):
        return all(li[j - 1] in {li[j], li[j] * 2, li[j] * 3} for j in range(1, len(li) + 1))
    return sat

if __name__ == "__main__":
    assert sat(sol())
