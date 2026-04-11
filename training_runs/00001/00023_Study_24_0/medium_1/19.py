def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 2

def sol():
    answer = []
    for i in range(10):
        answer.append(1 if i < 5 else 3)
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
