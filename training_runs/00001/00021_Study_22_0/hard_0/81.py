def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "string"

# print(sat(sol()))
!python -m test_case.checker_1 sol

if __name__ == "__main__":
    assert sat(sol())
