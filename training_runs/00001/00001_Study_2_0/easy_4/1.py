def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    return {'answer': 'correct'} if sat('yyyyyyyyyyyyyyyyyyyyyo') else {'answer': 'incorrect'}

# Checker
assert sat(sol()['answer'])

if __name__ == "__main__":
    assert sat(sol())
