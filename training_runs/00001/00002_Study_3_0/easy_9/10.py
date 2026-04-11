def sat(li: List[int]):
    return sorted(li) == list(range(1001))

def sol():
    li = list(range(1001))
    return sorted(li) == li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
