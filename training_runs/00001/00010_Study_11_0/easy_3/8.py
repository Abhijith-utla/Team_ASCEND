def sat(ls: List[float]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    return sat([1.0]*100)

def sat(ls: List[float]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
