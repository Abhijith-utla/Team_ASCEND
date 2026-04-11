def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    return [2, 3, 5, 7, 11, 13, 17, 19]

# This function checks if the list sat(answer) is correct
def is_sat(answer: List[int]):
    return sat(answer)

# This function constructs and returns a single answer value
def sol():
    return [2, 3, 5, 7, 11, 13, 17, 19]

# This assert statement checks if the function sol returns a valid answer
assert is_sat(sol())

if __name__ == "__main__":
    assert sat(sol())
