def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol() -> List[int]:
    return [1, 2, 3, 4] + [5] * 987 + [6]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
