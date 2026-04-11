def sat(s: str):
    return s.count('oo') >= 2

def sol():
    def sat(s: str):
        return s.count('oo') >= 2
    return sat

if __name__ == "__main__":
    assert sat(sol())
