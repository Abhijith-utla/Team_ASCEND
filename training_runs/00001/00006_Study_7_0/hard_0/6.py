def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "8^2888"

# Checker:
def main():
    import re
    assert sat(sol())

    test_strs = ["8^2888", "88^2888", "8^28888", "8^2888888", "18446744073709551616"]
    for s in test_strs:
        assert sat(s) == bool(re.fullmatch(r'^8\^2888$', s)), f"Expected {re.fullmatch(r'^8\^2888$', s)}, but got {sat(s)}"

main()

if __name__ == "__main__":
    assert sat(sol())
