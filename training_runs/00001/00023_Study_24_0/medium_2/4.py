def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    def sat(li: List[int]):
        return li.count(17) == 2 and li.count(3) == 1
    return [17, 3] if sat([]) else [3, 17]

if __name__ == "__main__":
    assert sat(sol())
