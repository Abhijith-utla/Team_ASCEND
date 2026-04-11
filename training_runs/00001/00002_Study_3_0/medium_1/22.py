def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    def sat(li: list[int]) -> bool:
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

    def gen():
        li = [0]*1000
        for i in range(1000):
            li[i] = i
        return li

    answer = gen()
    assert sat(answer)
    return answer

if __name__ == "__main__":
    assert sat(sol())
