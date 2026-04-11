def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return 16  # return the answer as an integer

if __name__ == "__main__":
    assert sat(sol())
