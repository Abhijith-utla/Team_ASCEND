def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    answer = {}
    answer['s'] = 'za'*99 + 'zo'*100 + 'z'*98
    return answer

assert sat(sol()['s'])

if __name__ == "__main__":
    assert sat(sol())
