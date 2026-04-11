def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    result = []
    for s in ['berlin', 'berg', 'lin', 'ger', 'berlin', 'ber', 'linber', 'l', 'inger', 'gerlin']:
        for t in ['berlin', 'berg', 'lin', 'ger', 'berlin', 'ber', 'linber', 'l', 'inger', 'gerlin']:
            if s != t:
                result.append(s + t)
    return result

if __name__ == "__main__":
    assert sat(sol())
