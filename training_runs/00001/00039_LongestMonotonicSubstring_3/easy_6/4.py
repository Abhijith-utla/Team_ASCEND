def sat(x: List[int], length: int, s: str):
    return all(s[x[i]] < s[x[i + 1]] for i in range(length - 1))

def sol():
    return [0]

def sat(x: List[int], length: int, s: str):
    return all(s[x[i]] < s[x[i + 1]] for i in range(length - 1))

# Test case
print(sat([0, 1], 2, 'ab'))  # False
print(sat([0, 0], 2, 'ab'))  # True

if __name__ == "__main__":
    assert sat(sol())
