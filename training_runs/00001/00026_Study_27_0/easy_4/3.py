def sat(li):
    return li[li[0]] != li[li[1]] and li[li[1]] != li[li[2]] and li[li[2]] == li[li[0]]

def sol():
    li = [1, 2, 3, 4, 5]
    while True:
        if sat(li):
            return li
        li[0], li[1], li[2] = li[2], li[0], li[1]
!

if __name__ == "__main__":
    assert sat(sol())
