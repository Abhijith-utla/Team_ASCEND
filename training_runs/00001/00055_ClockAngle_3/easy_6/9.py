def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# Test cases
assert sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert not sat([11, 59])
assert sat([11, 30])
assert sat([11, 31])
assert not sat([12, 0])
assert not sat([1, 0])
assert not sat([11, 60])
assert not sat([11, 61])
assert not sat([12, 0])
assert not sat([1, 60])
assert not sat([1, 61])
assert not sat([12, 0])
assert not sat([1, 0])
assert not sat([11, 0])
assert not sat([11, 30])
assert not sat([11, 31])
assert not sat([12, 0])
assert not sat([1, 0])
assert not sat([11, 0])
assert not sat([11, 30])
assert not sat([

if __name__ == "__main__":
    assert sat(sol())
