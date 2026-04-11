def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    return 998

# The output is 998 because the sorted list is [0, 1, 2, ..., 997] and the list is [0, 1, 2, ..., 999]
# The last number in the list is 997, not 998

if __name__ == "__main__":
    assert sat(sol())
