def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    import random
    def sat(li: List[int]):
        for _ in range(1000):
            random_li = [random.randint(0, 9) for _ in range(10)]
            if li != sorted(random_li):
                return False
        return True
    return sat

if __name__ == "__main__":
    assert sat(sol())
