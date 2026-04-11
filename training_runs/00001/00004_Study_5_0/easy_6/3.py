def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)])

    return sat([i for i in range(10)])

if __name__ == "__main__":
    assert sat(sol())
