def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return len(set(input().split())) == len(input().split())

# test case
assert sat(['apple', 'orange', 'banana'])
assert not sat(['apple', 'apple', 'banana'])

if __name__ == "__main__":
    assert sat(sol())
