def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    # Define the list
    li = [i for i in range(999)]
    # Return the sorted list
    return sorted(li)

if __name__ == "__main__":
    assert sat(sol())
