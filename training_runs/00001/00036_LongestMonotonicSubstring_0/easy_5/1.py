def sat(x: List[int], length=13):
    return len(x) >= length

def sol():
    return []

# Adding 10 random integers to the list
# This will ensure the length of the list is at least 13
x = [random.randint(1, 100) for _ in range(10)]
x.extend([random.randint(1, 100) for _ in range(10)])
assert sat(x)

# Extending the list to make its length 20
x.extend([random.randint(1, 100) for _ in range(10)])
assert sat(x)

# Extending the list again to make its length 30
x.extend([random.randint(1, 100) for _ in range(10)])
assert sat(x)

# Extending the list to make its length 40
x.extend([random.randint(1, 100) for _ in range(10)])
assert sat(x)

# Extending the list again to make its length 50
x.extend([random.randint(

if __name__ == "__main__":
    assert sat(sol())
