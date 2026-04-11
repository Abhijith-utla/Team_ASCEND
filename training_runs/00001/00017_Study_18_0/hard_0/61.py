def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    return 'berlin berger linber linger gerber gerlin'.split()

def sat(ls: List[str]):
    return all(x in ls for x in 'berlin berger linber linger gerber gerlin'.split())

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
