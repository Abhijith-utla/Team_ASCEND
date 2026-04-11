def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    return [s + t for s in ['berlin', 'berg', 'lin', 'ger'] for t in ['berlin', 'berg', 'lin', 'ger'] if s != t]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
