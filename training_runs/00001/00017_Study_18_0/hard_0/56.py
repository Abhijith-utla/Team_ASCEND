def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol(ls: List[str]):
    return ' '.join([''.join([s + t for s in ls if s != t]) for t in ls])

# Test the solution
assert sat(sol(['berlin', 'berg', 'lin', 'ger']))

if __name__ == "__main__":
    assert sat(sol())
