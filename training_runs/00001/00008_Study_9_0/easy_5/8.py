def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    li = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return li

print(sol()) # should return the list [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if __name__ == "__main__":
    assert sat(sol())
