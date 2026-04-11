def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    def sat(li: List[int]):
        return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

    li = [2] * 998 + [3]
    answer = None

    while not sat(li):
        if answer is not None:
            raise AssertionError(f"Previous answer: {answer}, Current answer: {li}")
        answer = li[:]
        li[0] += 1

    return answer

if __name__ == "__main__":
    assert sat(sol())
