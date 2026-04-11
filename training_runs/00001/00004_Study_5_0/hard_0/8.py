def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)])
    return sat([randint(0,9) for _ in range(100)])

if __name__ == "__main__":
    assert sat(sol())
