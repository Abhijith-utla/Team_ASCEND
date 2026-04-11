def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    answer = [i for i in range(10)]
    answer.insert(3, 2)
    return sat(answer)

if __name__ == "__main__":
    assert sat(sol())
