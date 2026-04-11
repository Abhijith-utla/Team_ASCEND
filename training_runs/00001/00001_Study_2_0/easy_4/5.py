def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    s = "y"*100 + "o"*101 + "y"*98
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
