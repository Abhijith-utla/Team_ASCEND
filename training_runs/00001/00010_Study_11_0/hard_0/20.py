def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    def sat(ls: List[str]):
        return min(ls) == max(ls) == str(len(ls))

    def gen():
        while True:
            yield [next(gen) for _ in range(10)]

    gen = gen()
    while True:
        ls = next(gen)
        if sat(ls):
            return ls

if __name__ == "__main__":
    assert sat(sol())
