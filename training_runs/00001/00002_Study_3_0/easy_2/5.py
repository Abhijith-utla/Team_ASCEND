def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

def sol() -> List[int]:
    return sorted(range(999))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
