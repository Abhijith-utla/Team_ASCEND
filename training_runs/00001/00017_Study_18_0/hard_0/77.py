def sat(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()

def sol():
    return [s + t for s in ['berlin', 'berger', 'linber', 'linger', 'gerber', 'gerlin'] for t in ['berlin', 'berger', 'linber', 'linger', 'gerber', 'gerlin'] if s != t]

# Testing the function
def test():
    result = sol()
    print(result)
    assert sat(result)

test()

if __name__ == "__main__":
    assert sat(sol())
