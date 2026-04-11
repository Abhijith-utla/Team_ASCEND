def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 2, 3, 4, 4, 4, 5]
    if sat(li):
        return 1
    else:
        return 0

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

print(sol())

if __name__ == "__main__":
    assert sat(sol())
