def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    def sat(s: str):
        return 'oo' in s and s.count('o') == 1000
    return sat

if __name__ == "__main__":
    assert sat(sol())
