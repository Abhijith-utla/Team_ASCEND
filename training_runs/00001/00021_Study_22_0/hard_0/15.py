def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return ''.join(s[::2] for s in str(int(input())))

# Checker code
def check_sol(s: str):
    return sat(s)

# Testing the sol function
print(check_sol(sol()))

if __name__ == "__main__":
    assert sat(sol())
