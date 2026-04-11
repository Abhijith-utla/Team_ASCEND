def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return sat

# Test cases
print(sol()("abc", "abcd", "abcde"))  # Expected: True
print(sol()("a", "aa", "aaa"))  # Expected: False

if __name__ == "__main__":
    assert sat(sol())
