def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

    def random_list():
        import random
        li = [random.randint(0, 999) for _ in range(1000)]
        return li

    li = random_list()

    while not sat(li):
        li = random_list()

    return li

if __name__ == "__main__":
    assert sat(sol())
