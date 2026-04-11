def sat(s: str):
    return len(s) == 1000 and s.count('o') == 1000

def sol():
    return {'answer': 'hello world'}

# Test the solution
assert sat(sol()['answer'])

if __name__ == "__main__":
    assert sat(sol())
