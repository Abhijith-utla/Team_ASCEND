def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Let's test our function with the given stamps and target.
assert sat([18, 1, 43, 81])
assert not sat([18, 1, 43])
assert not sat([18, 1, 44])
assert sat([1, 1, 1])
assert not sat([1, 1, 2])
assert not sat([1, 1])

# Now, we will create a list of 10 random stamps and check if our function works correctly.
import random
random_stamps = [random.randint(1, 100) for _ in range(10)]
assert sat(random_stamps)
assert not sat([random.randint(1, 100) for _ in range(11)])

if __name__ == "__main__":
    assert sat(sol())
