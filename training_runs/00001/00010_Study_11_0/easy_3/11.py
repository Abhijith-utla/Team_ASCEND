def sat(ls: List[float]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    def sat(ls: List[float]):
        if len(ls) == 0:
            return True
        else:
            return all(i in ls for i in range(len(ls)))

    return sat

# Checker code
assert sat([0.0, 1.0, 2.0])
assert not sat([0.0, 2.0])
assert sat([1.0, 2.0, 3.0])
assert not sat([])

if __name__ == "__main__":
    assert sat(sol())
