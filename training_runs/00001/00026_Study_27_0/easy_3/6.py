def sat(li):
    return li[li[0]] < li[li[1]]

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
