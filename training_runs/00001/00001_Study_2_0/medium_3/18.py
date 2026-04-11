def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    return {'answer': 'The string has exactly 100 occurrences of "z" and 101 occurrences of "zo" and 98 occurrences of "zz"'}

# Test the function
assert sat(sol()['answer'])

if __name__ == "__main__":
    assert sat(sol())
