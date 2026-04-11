def sat(s: str):
    return s.count('x') == 100 and s.count('o') == 111 and s.count('xx') == 98

def sol():
    s = 'ooo' * 100 + 'x' * 111 + 'xx' * 98
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
