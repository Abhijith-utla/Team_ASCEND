def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])

    assert sat([]), "List is not a solution"
    assert sat([1]), "List is not a solution"
    assert sat([1, 1]), "List is not a solution"
    assert not sat([1, 2]), "List is a solution"
    assert sat([1, 2, 3]), "List is not a solution"
    assert not sat

if __name__ == "__main__":
    assert sat(sol())
