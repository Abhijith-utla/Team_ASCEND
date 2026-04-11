def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

    result = []
    for _ in range(100):
        li = [randint(0, 9) for _ in range(10)]
        if sat(li):
            result.append(li)

    return result

if __name__ == "__main__":
    assert sat(sol())
