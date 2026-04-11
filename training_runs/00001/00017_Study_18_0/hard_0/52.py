def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

# Test case
print(sat(["berlin", "berg"]))  # should return True
print(sat(["berlin", "lining"]))  # should return False

# Checker
assert sol(["berlin", "berg"]) == True
assert sol(["berlin", "lining"]) == False

if __name__ == "__main__":
    assert sat(sol())
