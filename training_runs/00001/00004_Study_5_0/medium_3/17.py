def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

    result = sat()
    assert result
    return result

if __name__ == "__main__":
    assert sat(sol())
