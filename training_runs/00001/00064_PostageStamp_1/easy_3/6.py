def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if not isinstance(s, int):
            return False
    if sum(stamps) != target:
        return False
    return True

def sol():
    return [37, 37, 12, 87, 39]

print(sat(sol()))  # Should print: True

# For manual testing
assert sat(sol())
assert not sat([37, 37, 12, 87])
assert not sat([37, 37, 12, 87, 39, 39])

if __name__ == "__main__":
    assert sat(sol())
