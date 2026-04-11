def sat(li: List[int]):
    return all(x == li[i] for i in range(len(li)))

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())
