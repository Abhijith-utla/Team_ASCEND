def sat(li: List[int]):
    return all(li.index(x) < sum(li[:li.index(x)]) for x in set(li))

def sol():
    def sat(li: List[int]):
        return all(li.index(x) < sum(li[:li.index(x)]) for x in set(li))

    return sat

if __name__ == "__main__":
    assert sat(sol())
