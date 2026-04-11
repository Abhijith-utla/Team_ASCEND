def sat(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

def sol():
    s = 'aaa' * 200 + 'aa' * 201 + 'a' * 198
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
