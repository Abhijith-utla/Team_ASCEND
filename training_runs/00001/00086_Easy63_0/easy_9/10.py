def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 1 and s.count("1") == 4 and eval(s) == 18 * 1

def sol():
    return "18+11"

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
