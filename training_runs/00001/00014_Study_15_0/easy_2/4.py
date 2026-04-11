def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

def sol():
    li = [i for i in range(20)]
    return li

if __name__ == "__main__":
    assert sat(sol())
