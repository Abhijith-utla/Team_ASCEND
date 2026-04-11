def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    li = list(range(999))
    li[0] = -1  # This line is to modify the first element of the list
    return li

if __name__ == "__main__":
    assert sat(sol())
