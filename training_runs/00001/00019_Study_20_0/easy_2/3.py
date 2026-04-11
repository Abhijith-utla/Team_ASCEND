def sat(li: List[int]):
    # Check if all elements in the list are either 1, 2, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol(li: List[int]) -> int:
    for i in range(1, len(li) + 1):
        if i not in {li[j - 1] - 1 for j in range(1, len(li) + 1)} and \
           i not in {li[j + 1] + 1 for j in range(1, len(li) + 1)} and \
           i not in {3 * li[j - 1] for j in range(1, len(li) + 1)} and \
           i not in {3 * li[j + 1] for j in range(1, len(li) + 1)}:
            return i
    return None

if __name__ == "__main__":
    assert sat(sol())
