def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    ls = [str(i) for i in range(10)]  # Correct pattern: Min and max are equal and the length is also equal.
    return min(ls) == max(ls) == str(len(ls))

# Check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
