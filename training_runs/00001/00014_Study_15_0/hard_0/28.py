def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return [x for x in range(20) if sum(range(x+1)) == 2 ** x - 1]

if __name__ == "__main__":
    assert sat(sol())
