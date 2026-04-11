def sat(x: List[int], length=1):
    return all(x[i] < x[i + 1] for i in range(length))

def sol():
    return []

def sol(x):
    if not sat(x):
        return []
    res = [x[0]]
    for i in range(1, len(x)):
        if x[i] < res[-1]:
            res.append(x[i])
    return res

if __name__ == "__main__":
    assert sat(sol())
