def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    answer = 1
    while sat(answer):
        answer += 1
    return answer

def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
