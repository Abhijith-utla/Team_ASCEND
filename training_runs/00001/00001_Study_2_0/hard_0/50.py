def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    return {
        'answer': 'The string contains 1000 "o"s and 100 "oo"s and 801 "ho"s.'
    }

# Test the function
assert sat(sol()['answer'])

if __name__ == "__main__":
    assert sat(sol())
