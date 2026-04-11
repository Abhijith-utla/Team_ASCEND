def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s) and s.index(s[0]) == s.index(s[-1])

def sol():
    return "success"

# Assign the function to a variable for testing
sol_func = sol

# Test the function
assert sol_func() == "success"

if __name__ == "__main__":
    assert sat(sol())
