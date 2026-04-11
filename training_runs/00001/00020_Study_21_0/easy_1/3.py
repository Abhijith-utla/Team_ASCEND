def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    li = [random.randint(1, 9) for _ in range(9)]
    while not sat(li):
        li = [random.randint(1, 9) for _ in range(9)]
    return li

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

answer = sol()
assert sat(answer)

print(answer)

if __name__ == "__main__":
    assert sat(sol())
