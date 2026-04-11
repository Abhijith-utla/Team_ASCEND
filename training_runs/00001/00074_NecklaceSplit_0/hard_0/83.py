def sat(n: int, lace="bbrbrbbbbbbrrrrrrrbrrrrbbbrbrrbbbrbrrrbrrbrrbrbbrrrrrbrbbbrrrbbbrbbrbbbrbrbb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

# The function 'sol' is already defined by the user.
# The function 'sol' does not take any arguments.
# The function 'sol' returns an answer object.
# The final checker will run: assert sat(sol())
# The output must be valid Python code only.

# Correct pattern:
def sol():
    return ""

# Incorrect pattern:
def sol(x):
    ...

if __name__ == "__main__":
    assert sat(sol())
