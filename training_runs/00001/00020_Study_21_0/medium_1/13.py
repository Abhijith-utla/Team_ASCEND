def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    def check(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

    for _ in range(1000):
        li = [random.randint(1, 9) for _ in range(10)]
        if not check(li):
            continue
        for i in range(10):
            for j in range(i + 1, 10):
                li[i], li[j] = li[j], li[i]
                if check(li):
                    return li
                li[i], li[j] = li[j], li[i]
    return []

if __name__ == "__main__":
    assert sat(sol())
