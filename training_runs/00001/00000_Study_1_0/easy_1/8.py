def sat(s: str):
    return len(s) == 1000 and s.count('o') == 1000

def sol():
    return {"answer": "success"}

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
