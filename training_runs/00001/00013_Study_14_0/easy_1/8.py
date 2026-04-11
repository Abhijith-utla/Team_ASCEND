def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

def sol():
    def sat(li: List[int]):
        return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

    result = []
    for _ in range(1000):
        li = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
        result.append(sat(li))
    return all(result)

if __name__ == "__main__":
    assert sat(sol())
