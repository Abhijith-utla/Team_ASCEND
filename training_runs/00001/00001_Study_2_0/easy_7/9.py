def sat(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

def sol():
    s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
