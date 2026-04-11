def sat(s: str):
    return 'o' in s and 'oo' not in s and s.count('o') == 1000

def sol():
    return Answer(True)

# Test the function
def test_sol():
    assert sat(sol().val)

test_sol()

if __name__ == "__main__":
    assert sat(sol())
