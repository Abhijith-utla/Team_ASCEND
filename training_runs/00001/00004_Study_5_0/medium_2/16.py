def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    answer = sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10])
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
