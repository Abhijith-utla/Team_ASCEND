def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 2 and s.count("1") == 1 and eval(s) == 63

def sol():
    return "818"

# The function 'sat' is already defined by the user.
# So, there is no need to define it again.

if __name__ == "__main__":
    assert sat(sol())
