def sat(x: List[int], length: int, s: str):
    return all(s[x[i]] < s[x[i + 1]] for i in range(length - 1))

def sol():
    return [0, 1, 2, 3, 4]

# Testing the function
assert sat(sol(), 5, "abcde")
assert not sat(sol(), 5, "ebcda")

if __name__ == "__main__":
    assert sat(sol())
