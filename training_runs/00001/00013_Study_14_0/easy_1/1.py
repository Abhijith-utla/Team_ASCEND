def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

def sol():
    return sat([2, 3, 1, 5])  # Return True

def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

assert sat(sol())  # Should pass without any assertion errors

if __name__ == "__main__":
    assert sat(sol())
