def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'Hello' and 'o' * 1000

print(sol())

if __name__ == "__main__":
    assert sat(sol())
