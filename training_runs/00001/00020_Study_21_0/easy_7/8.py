def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(7)])
    return sat

if __name__ == "__main__":
    assert sat(sol())
