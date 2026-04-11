def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    return {
        'answer': 'String contains 1000 occurrences of "o" and 100 occurrences of "oo" and 801 occurrences of "ho".'
    }

# Test the function
def test_sat():
    assert sat(sol()['answer'])

test_sat()

if __name__ == "__main__":
    assert sat(sol())
