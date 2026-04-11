def sat(s: str):
    return len(s) == 1000 and 'o' in s

def sol():
    return {'answer': 'Hello, World!'}

if __name__ == "__main__":
    assert sat(sol())
