def sat(ls: List[str]):
    return all(len(s) == 8 for s in ls)

def sol():
    return "Success"

# Testing
assert sat(sol()) == True

if __name__ == "__main__":
    assert sat(sol())
