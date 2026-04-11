def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol(s: str):
    return {'count_y': s.count('y'), 'count_yo': s.count('yo')}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
