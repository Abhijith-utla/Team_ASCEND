def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    li = [2, 3, 4, 5, 6]
    return sat(li)

# Correct pattern
# def sol():
#     li = [2, 3, 4, 5, 6]
#     return sat(li)

if __name__ == "__main__":
    assert sat(sol())
