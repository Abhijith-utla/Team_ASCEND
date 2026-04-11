def sat(li: List[int]) -> bool:
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    answer = [3, 6, 9]
    return answer

print(sol())

# Assertion check
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
