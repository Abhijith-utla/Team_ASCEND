def sat(li):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]] and li[li[2]] != li[li[0]]

def sol():
    return [sat([1, 2, 3, 4, 5]), sat([1, 3, 2, 4, 5]), sat([1, 2, 3, 5, 4]), sat([1, 2, 4, 3, 5]), sat([1, 2, 4, 5, 3]), sat([5, 1, 3, 2, 4]), sat([5, 3, 1, 2, 4]), sat([5, 3, 2, 4, 1]), sat([5, 1, 2, 4, 3]), sat([5, 2, 1, 3, 4]), sat([5, 2, 3, 4, 1]), sat([5, 2, 3, 1, 4]), sat([5, 2, 4, 1, 3]), sat([5, 4, 1, 2, 3]), sat([5, 4, 2,

if __name__ == "__main__":
    assert sat(sol())
