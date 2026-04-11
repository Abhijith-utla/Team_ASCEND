def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    li = [i for i in range(999)]
    return li

# Uncomment the following line to run the assertion
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
