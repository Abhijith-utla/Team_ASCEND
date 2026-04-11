def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    ls = ['berlin', 'berger', 'linber', 'linger', 'gerber', 'gerlin']
    return ls

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
