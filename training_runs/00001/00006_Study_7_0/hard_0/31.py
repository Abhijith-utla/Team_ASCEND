def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "888"

# Test cases
assert sat(sol())
assert not sat("123")
assert not sat("888")
assert not sat("88")
assert not sat("889")

if __name__ == "__main__":
    assert sat(sol())
