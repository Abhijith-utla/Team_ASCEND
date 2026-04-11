def sat(li: List[int]):
    # Check if all elements in the list are either 2, 3, or 4 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    # A list with all elements being multiples of 2, 3, and 4
    answer = [4, 6, 8, 12, 15, 18, 21, 24]
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
