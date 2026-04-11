def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    count_y = lambda s: s.count('y')
    count_yo = lambda s: s.count('yo')
    count_yy = lambda s: s.count('yy')
    
    s = 'yyyyyyyyyyyyyyyyyyyyy'  # Define the string here
    
    return count_y(s) == 100 and count_yo(s) == 101 and count_yy(s) == 98

if __name__ == "__main__":
    assert sat(sol())
