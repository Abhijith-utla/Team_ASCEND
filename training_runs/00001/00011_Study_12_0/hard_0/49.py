def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [4] + [i for i in range(1, 1000) if i not in [4, 9, 14, 19, 24, 39, 44, 49, 54, 69, 74, 79, 84, 99, 104, 109, 114, 119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 169, 174, 179, 184, 189, 194, 199, 204, 209, 214, 219, 224, 229, 234, 239, 244, 249, 254

if __name__ == "__main__":
    assert sat(sol())
