def sat(li):
    return li[li[0]] != li[li[1]]

def sol():
    return [sat([1, 2, 3, 4]), sat([1, 3, 3, 4]), sat([1, 3, 3, 5]), sat([1, 2, 2, 4]), sat([1, 2, 3, 3]), sat([2, 2, 3, 4]), sat([1, 1, 3, 4]), sat([1, 2, 2, 5]), sat([1, 2, 3, 2]), sat([1, 2, 3, 3])]

def sat(li):
    return li[li[0]] != li[li[1]]

if __name__ == "__main__":
    assert sat(sol())
