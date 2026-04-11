def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return "not_a_string" in [1, 2, 3, 4, 5] and "not_a_string" != 1

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
