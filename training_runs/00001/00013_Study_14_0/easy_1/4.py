def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

def sol():
    return [i for i in range(1, 11) if not sat([i]*i)]

def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

if __name__ == "__main__":
    assert sat(sol())
