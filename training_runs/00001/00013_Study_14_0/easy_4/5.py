def sat(li: List[int]):
    return all(li.index(x) < sum(li[:li.index(x)]) for x in set(li))

def sol():
    def sat(li: List[int]):
        for i in range(1, len(li)):
            if li[i] < li[i-1]:
                return False
        return True

    return sat

if __name__ == "__main__":
    assert sat(sol())
