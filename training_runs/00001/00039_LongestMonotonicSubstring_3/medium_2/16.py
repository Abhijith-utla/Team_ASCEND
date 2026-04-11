def sat(x: List[int], length=0, s=""):
    return all(s[x[i]] < s[x[i + 1]] for i in range(length - 1))

def sol():
    return {"output": "ok"}

if __name__ == "__main__":
    assert sat(sol())
