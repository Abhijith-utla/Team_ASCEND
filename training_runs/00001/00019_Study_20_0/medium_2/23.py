def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return {"answer": False}

def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def main():
    assert sat(sol())

main()

if __name__ == "__main__":
    assert sat(sol())
