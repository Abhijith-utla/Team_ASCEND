def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    return {"answer": sum(range(20))}

if __name__ == "__main__":
    assert sat(sol())
