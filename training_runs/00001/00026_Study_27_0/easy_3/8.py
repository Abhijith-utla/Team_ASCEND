def sat(li):
    return li[li[0]] < li[li[1]]

def sol():
    return [1, 0, 3, 2]

if __name__ == "__main__":
    assert sat(sol())
