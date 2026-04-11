def sat(li):
    return li[li[0]] == li[li[1]] and li[li[1]] != li[li[2]] and li[li[2]] != li[li[0]]

def sol():
    li = [1, 2, 3]
    while not sat(li):
        li[0] += 1
        li[0] %= 3
    return li[0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
