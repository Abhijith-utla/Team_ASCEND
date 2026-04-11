def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol() -> bool:
    return sat([0]*20)

def sat(li: List[int]) -> bool:
    return all(x == sum(li[:i]) for i in range(20))

if __name__ == "__main__":
    assert sat(sol())
