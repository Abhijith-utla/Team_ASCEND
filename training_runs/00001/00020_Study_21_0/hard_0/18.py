def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3]

# The function sat is already defined by the user and is used to check the solution.
# We need to write the sol function ourselves.
# The sol function here simply returns a list of integers [1, 2, 3].

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
