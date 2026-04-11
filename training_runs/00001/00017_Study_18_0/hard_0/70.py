def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    return [s + t for s in ['berlin', 'berger', 'linber', 'gerber', 'gerlin'] for t in ['berlin', 'berger', 'linber', 'gerber', 'gerlin'] if s != t] == 'berlin berger linber linger gerber gerlin'.split()

if __name__ == "__main__":
    assert sat(sol())
