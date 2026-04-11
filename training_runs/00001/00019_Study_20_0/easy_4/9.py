def sat(li: List[int]) -> bool:
    return len(li) == len(set(li))

def sol():
    return len(set(input().split()))

# Test
assert sat(sol(['1', '2', '2', '3', '4', '4', '5', '5']))
assert not sat(sol(['1', '2', '3', '4', '5']))

if __name__ == "__main__":
    assert sat(sol())
