def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [i % 10 for i in range(1000)]  # a list with 1000 integers from 0 to 9
    return sum(li) == 450  # check if the sum of the list is 450

if __name__ == "__main__":
    assert sat(sol())
