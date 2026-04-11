def sat(li):
    return li[li[0]] != li[li[1]]

def sol():
    return [sat, [0, 1]]

def sat(li):
    return li[li[0]] != li[li[1]]

if __name__ == "__main__":
    assert sat(sol())
