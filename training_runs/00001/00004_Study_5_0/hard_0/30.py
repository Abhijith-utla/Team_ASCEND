def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
