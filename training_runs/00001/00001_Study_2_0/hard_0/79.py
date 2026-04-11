def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    def sat(s: str):
        return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

    s = 'ho' * 801 + 'o' * 1000
    return sat(s)

if __name__ == "__main__":
    assert sat(sol())
