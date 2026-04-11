def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    return {'count_of_y': 100, 'count_of_yo': 101, 'count_of_yy': 98}

print(sol())

if __name__ == "__main__":
    assert sat(sol())
