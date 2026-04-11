def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

def sol():
    def sat(s: str):
        return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98
    
    s = ''
    while len(s) < 500:
        s += 'y'
        if sat(s):
            break
    
    s += 'yo' * 101
    if not sat(s):
        return None
    
    s = ''
    while len(s) < 1000:
        s += 'y'
        if sat(s):
            break
    
    s += 'yy' * 100
    if not sat(s):
        return None
    
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
