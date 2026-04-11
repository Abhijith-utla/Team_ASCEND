def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    answer = []
    for i in range(100):
        answer.append(17 if i < 50 else 3)
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
