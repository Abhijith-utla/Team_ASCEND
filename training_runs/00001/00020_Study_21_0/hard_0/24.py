def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    from random import randint

    def gen_list():
        lst = [randint(0, 10) for _ in range(10)]
        lst[0] = lst[-1]
        return lst

    def check(lst: List[int]):
        return all([lst[i] != lst[i + 1] for i in range(10)]) and len(set(lst)) == 3

    while True:
        lst = gen_list()
        if check(lst):
            return lst

if __name__ == "__main__":
    assert sat(sol())
