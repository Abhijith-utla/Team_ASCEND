def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return ""

# Correct pattern
def sol(s: str):
    return s[::-1]

# Incorrect pattern
def sol(s: str):
    return s

if __name__ == "__main__":
    assert sat(sol())
