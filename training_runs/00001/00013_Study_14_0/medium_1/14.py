def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([i < sum(li[:i]) for i in range(20)])
    return sat

if __name__ == "__main__":
    assert sat(sol())
