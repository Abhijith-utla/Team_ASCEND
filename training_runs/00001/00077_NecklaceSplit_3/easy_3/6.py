def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n - 1)

def sol():
    return {'answer': 'r' * (2 * 0 - 1)}

# checker
assert sat(sol()['answer'])

if __name__ == "__main__":
    assert sat(sol())
