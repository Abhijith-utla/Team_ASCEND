def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol(li: List[int]):
    # Check if the list length is 1000
    if len(li) != 1000:
        raise ValueError("The length of the list should be 1000.")

    # Check if the sum of each element and its index is equal to 1
    if not all(i + j == 1 for i, j in enumerate(li)):
        raise ValueError("The sum of each element and its index should be 1.")

    # Return the first element of the list
    return li[0]

if __name__ == "__main__":
    assert sat(sol())
