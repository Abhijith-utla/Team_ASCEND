def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    import random
    def gen_list():
        ls = [random.randint(0, 100) for _ in range(1000)]
        return ls

    def check_answer(ls):
        idx1 = random.randint(0, 99)
        idx2 = random.randint(0, 99)
        value = ls[idx1]
        while idx1 == idx2 or ls[idx1] == value:
            idx2 = random.randint(0, 99)
        return sat(ls, idx1, idx2, value)

    ls = gen_list()
    return check_answer(ls)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
