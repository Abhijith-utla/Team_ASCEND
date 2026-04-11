def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)] and len(set(li)) == 3)

def sol():
    li = [3, 2, 1, 3, 2, 1, 4, 4]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
