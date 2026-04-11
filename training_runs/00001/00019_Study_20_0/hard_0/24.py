def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return 5

# Assuming that `sat` is a function that checks if the list satisfies the condition given in the problem.
# For example, in this case, we can simply return 5 as the solution.
# In the real problem, we will have to implement the function `sat` based on the problem's requirements.

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
