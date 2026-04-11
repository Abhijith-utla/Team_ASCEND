def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

    # Create a list of 1000 numbers
    li = [i for i in range(999)]

    # Check if the list is a permutation
    if not sat(li):
        return False

    return True

if __name__ == "__main__":
    assert sat(sol())
