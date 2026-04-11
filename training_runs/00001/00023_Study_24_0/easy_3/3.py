def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    answer = [17, 3, 17, 17, 17, 3, 3, 3, 3, 3]
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
