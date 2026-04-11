def sat(li: List[int]):
    return max(li) == 34

def sol():
    return 34

# This assert statement is used to test the correctness of our solution.
# It will pass if the solution is correct, fail otherwise.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
