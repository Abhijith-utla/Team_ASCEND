def sat(li: List[int]):
    return li.count(1) == 2 and li.count(2) == 2 and li.count(3) == 2 and li.count(4) == 2 and li.count(5) == 2 and li.count(6) == 2 and li.count(7) == 2 and li.count(8) == 2 and li.count(9) == 2

def sol():
    answer = []
    for i in range(1, 10):
        answer.append(i)
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
