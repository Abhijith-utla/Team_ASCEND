def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    li = [0]*999
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
