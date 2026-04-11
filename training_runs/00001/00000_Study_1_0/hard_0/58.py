def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    return {'answer': 'Valid'} if sat('oo' * 1000) else {'answer': 'Invalid'}

def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

if __name__ == "__main__":
    print(sol())

if __name__ == "__main__":
    assert sat(sol())
