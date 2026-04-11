def sat(li: List[int]) -> bool:
    return all(i != 0 for i in li)

def sol():
    return [i for i in range(1, 101) if sat([i])]

if __name__ == "__main__":
    assert sat(sol())
