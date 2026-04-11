def sat(li: List[str]):
    return all(len(i) <= 5 for i in li) and all(i.isalpha() for i in li)

def sol(li: List[str]):
    return all(len(i) <= 5 and i.isalpha() for i in li)

def sat(li: List[str]):
    return sol(li)

# Test case
print(sat(["abcde", "abc", "xyz"]))  # Expected output: True
print(sat(["abcdef", "abc", "xyz"]))  # Expected output: False

if __name__ == "__main__":
    assert sat(sol())
