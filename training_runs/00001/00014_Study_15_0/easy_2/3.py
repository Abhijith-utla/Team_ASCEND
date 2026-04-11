def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

def sol():
    li = [10, 20, 15]
    assert sat(li)
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
