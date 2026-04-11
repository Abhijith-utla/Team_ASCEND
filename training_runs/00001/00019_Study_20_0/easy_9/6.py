def sat(li: List[int]) -> bool:
    return all(i == 3 * j for j, i in enumerate(li))

def sol():
    li = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    return sat(li)

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
