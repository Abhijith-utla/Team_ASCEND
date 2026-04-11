def sat(s: str):
    return s.count('x') == 110 and s.count('o') == 101 and s.count('xx') == 98

def sol():
    return {'answer': 'yes'}

# Testing
def test_sol():
    assert sat(sol()['answer'])

# Run the test
test_sol()

if __name__ == "__main__":
    assert sat(sol())
