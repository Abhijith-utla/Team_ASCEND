def sat(x: List[int], s: str):
    return all(s[i] <= s[i + 1] for i in range(len(x) - 1))

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert sat(sol(), 'abcdefghij')

if __name__ == "__main__":
    assert sat(sol())
