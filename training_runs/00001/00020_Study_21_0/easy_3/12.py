def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 1]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
