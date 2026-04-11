def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [i for i in range(len('O!A{SeKv')) if 'O!A{SeKv'[i] <= 'O!A{SeKv'[i + 1] and 'O!A{SeKv'[i + 1] > 'O!A{SeKv'[i]]]

if __name__ == "__main__":
    assert sat(sol())
