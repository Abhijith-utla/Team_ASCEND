def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if sat(li):
            return li
        else:
            for i in range(9):
                if li[i] < li[i + 1]:
                    li[i], li[i + 1] = li[i + 1], li[i]
                    break
                else:
                    li[i], li[i + 1] = li[i + 1], li[i]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
