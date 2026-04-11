def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    return 'berlin berger linber linger gerber gerlin' == ' '.join(' '.join(sorted(w)) for w in 'berlin berger linber linger gerber gerlin'.split() for s in 'berlin berger linber linger gerber gerlin'.split())

def test():
    assert sat(sol())

test()

if __name__ == "__main__":
    assert sat(sol())
