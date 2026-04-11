def sat(li):
    return li[li[0]] != li[li[1]]

def sol():
    return [5, 3, 2, 1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
