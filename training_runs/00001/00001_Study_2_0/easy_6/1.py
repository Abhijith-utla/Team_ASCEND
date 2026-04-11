def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

def sol():
    return {
        'count_yy': 'Count of "yy" is 100',
        'count_yo': 'Count of "yo" is 101',
        'count_y': 'Count of "y" is 98'
    }

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
