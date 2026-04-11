def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    def sat(li: List[int]):
        return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

    return sat

if __name__ == "__main__":
    assert sat(sol())
