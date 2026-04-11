def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    li = [0] * 10  # Create a list of 10 zeros
    return li

if __name__ == "__main__":
    assert sat(sol())
