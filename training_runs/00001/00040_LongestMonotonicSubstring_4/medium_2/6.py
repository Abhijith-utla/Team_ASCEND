def sat(x: List[int], s: str):
    return all(s[i] <= s[i + 1] for i in range(len(x) - 1))

def sol():
    x = [3, 1, 4, 1, 5, 9]
    s = 'geeksforgeeks'
    assert sat(x, s)
    return x, s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
