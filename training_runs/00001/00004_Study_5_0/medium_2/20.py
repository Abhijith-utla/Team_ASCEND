def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    def sat(li: List[int]):
        for i in range(1, 11):
            if li.count(i) != i:
                return False
        return True

    return sat

if __name__ == "__main__":
    assert sat(sol())
