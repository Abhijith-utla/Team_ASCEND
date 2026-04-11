def sat(li: List[int]):
    return all(li[i] < sum(li[:i-1]) if i > 0 else li[i] < sum(li) for i in range(len(li)))

def sol():
    def sum_until(li, idx):
        return sum(li[:idx])

    def check(li):
        for i in range(1, len(li)):
            if li[i] < sum_until(li, i):
                return False
        return True

    def gen():
        li = [i + 1 for i in range(10)]
        while not check(li):
            li[-1] += 1
            for i in range(len(li) - 1, -1, -1):
                if li[i] > 10:
                    li[i - 1] += li[i] // 10
                    li[i] %= 10
                if len(li) > i + 1 and li[i + 1] > 10:
                    li[i + 1] += li[i] // 10
                    li[i] %= 10
            li = [i + 1 for i in li]
        return li

    return gen()

print(sol())

if __name__ == "__main__":
    assert sat(sol())
