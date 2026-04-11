def sat(li):
    return li[li[0]] < li[li[1]]

def sol():
    return [3, 1]

def sat(li):
    return li[li[0]] < li[li[1]]

if not sat(sol()):
    raise AssertionError('Function does not satisfy the constraints.')

if __name__ == "__main__":
    assert sat(sol())
