def sat(li):
    return li[li[0]] < li[li[1]]

def sol():
    li = [5, 3, 2, 1]
    return li[li[0]] < li[li[1]]

if __name__ == "__main__":
    assert sat(sol())
