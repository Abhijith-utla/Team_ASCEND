def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol(ls: List[str]):
    return ' '.join(ls[i] + ls[-i-1] for i in range(len(ls)))

def sat(ls: List[str]):
    return sol(ls) == 'berlin berger linber linger gerber gerlin'.split()

if __name__ == "__main__":
    assert sat(sol())
