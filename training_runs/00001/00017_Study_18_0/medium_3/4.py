def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return len(set(input().split()))

# Testing
assert sat(sol(['apple', 'banana', 'apple']))
assert not sat(sol(['apple', 'banana', 'grape']))

if __name__ == "__main__":
    assert sat(sol())
