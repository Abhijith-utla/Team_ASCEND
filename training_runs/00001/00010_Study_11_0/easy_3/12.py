def sat(ls: List[float]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    return [i for i in range(10) if i not in sat([i])]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
