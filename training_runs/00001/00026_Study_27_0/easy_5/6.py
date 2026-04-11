def sat(li):
    return li[li[0]] == li[li[1]] and li[li[1]] != li[li[2]] and li[li[2]] != li[li[0]]

def sol():
    li = [1, 2, 3]
    while True:
        for i in range(3):
            for j in range(i+1, 3):
                li[i], li[j] = li[j], li[i]
                if sat(li):
                    return li
                li[i], li[j] = li[j], li[i]
sol()

if __name__ == "__main__":
    assert sat(sol())
