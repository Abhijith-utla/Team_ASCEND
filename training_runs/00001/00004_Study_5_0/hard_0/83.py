def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol() -> List[int]:
    return [i for i in range(10) if i % 2 == 0]

if __name__ == "__main__":
    assert sat(sol())
