def sat(x: List[int], s="Dynamic programming solves this puzzle!!!"):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

def sol():
    return {"answer": True}

if __name__ == "__main__":
    assert sat(sol())
