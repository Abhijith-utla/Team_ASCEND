def sat(li):
    return li[li[0]] == li[li[1]]

def sol():
    li = [2, 5, 1, 9, 3, 7]
    return li[li[0]] == li[li[1]]

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
