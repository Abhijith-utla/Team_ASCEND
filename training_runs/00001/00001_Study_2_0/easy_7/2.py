def sat(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

def sol(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

# Test the function
assert sat("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
assert not sat("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
assert not sat("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab")

if __name__ == "__main__":
    assert sat(sol())
