def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    return []

# Incorrect pattern
# def sol(x):
#     return [x]

# Incorrect pattern
# def sol(li: List[int], x: int):
#     return [li, x]

# Correct pattern
# def sol(li: List[int]):
#     return [li]

# Incorrect pattern
# def sol(li: List[int], x: int, y: int):
#     return [li, x, y]

# Correct pattern
# def sol(li: List[int]):
#     return [li]

# Incorrect pattern
# def sol(li: List[int], x: int):
#     return [li, x]

# Correct pattern
# def sol(li: List[int]):
#     return [li]

# Incorrect pattern
# def sol(li: List[int], x: int, y: int, z: int):
#     return [li, x, y, z]

# Correct pattern
# def sol(li: List[int

if __name__ == "__main__":
    assert sat(sol())
