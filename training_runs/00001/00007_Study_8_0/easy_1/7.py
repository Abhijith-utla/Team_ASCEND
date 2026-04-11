def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    return {"answer": True}

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
