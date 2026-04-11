def sat(l: List[int]):
    return all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) and len(set(l)) > 995

def sol():
    return []

# This is just a placeholder to check if the given solution is correct.
# The real solution should be inserted in the sol() function.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
