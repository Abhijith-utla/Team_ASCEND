def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return {1: 2, 3: 4}

# Correct pattern:
# def sol():
#     return {1: 2, 3: 4}

# Incorrect pattern:
# def sol(li: List[int]):
#     return all(j in {i} for i, j in enumerate(li))

if __name__ == "__main__":
    assert sat(sol())
