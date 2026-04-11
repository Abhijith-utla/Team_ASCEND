def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n - 1)

def sol():
    return {
        "n": 1,
        "answer": "r" * (1 - 1)
    }

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
