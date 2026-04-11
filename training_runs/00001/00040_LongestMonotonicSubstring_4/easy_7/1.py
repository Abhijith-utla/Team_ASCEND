def sat(x: List[int], l: int, s: str):
    return all(s[i] <= s[i + 1] for i in range(l))

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

if __name__ == "__main__":
    assert sat(sol())
