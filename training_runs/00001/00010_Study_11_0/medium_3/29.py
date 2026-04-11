def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return [1, 2, 3]

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
