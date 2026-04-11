def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    def check(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3
    li = [random.randint(1, 10) for _ in range(11)]
    li[0] = li[1]
    while not check(li):
        li[random.randint(1, 10)] = random.randint(1, 10)
    return li

if __name__ == "__main__":
    assert sat(sol())
