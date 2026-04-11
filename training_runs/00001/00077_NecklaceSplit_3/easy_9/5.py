def sat(n: int, lace="bbbbrrbbrrbbrrbbrrbbb"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 1

# This assert statement does not work, as we cannot test a Python function. 
# We can only test the code. If the function `sol` works as expected, this assert statement will not raise an error.
assert sat(1)

if __name__ == "__main__":
    assert sat(sol())
