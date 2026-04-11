def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

if __name__ == "__main__":
    assert sat([])
    assert not sat([(5, 10)])
    assert sat([(5, 10), (6, 12), (7, 14), (8, 16)])
    assert not sat([(5, 10), (6, 11), (7, 13), (8, 15)])
    assert sat([(5, 10), (6, 11), (7, 13), (8, 15), (9, 17), (10, 19), (11, 21)])
    assert not sat([(5, 10), (6, 11), (7, 13), (8, 15), (9, 17), (10, 18)])

This is a simple test, we are checking if our function works on various inputs. Note that `sat` function is defined to return a list, so we cannot directly return a solution without

if __name__ == "__main__":
    assert sat(sol())
