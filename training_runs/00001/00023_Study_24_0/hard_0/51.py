def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    answer = [1, 1, 1, 3, 3, 3]
    return answer

if __name__ == "__main__":
    assert sat(sol())
