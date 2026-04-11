def sat(quine: str):
    return eval(quine) == quine

def sol():
    return ""

# This is the test that the checker will run.
# You should write your own assert statements to test your solution.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
