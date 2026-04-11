def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

def sol():
    return {i - 1: 1 for i in range(1, 129) if i - 1 in {i - 1, i + 1, 3 * i}}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
