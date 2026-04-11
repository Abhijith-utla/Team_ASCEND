def sat(li: List[int]):
    return all(x == li[i] for i in range(len(li)))

def sol():
    def sat(li: List[int]):
        return all(x == li[i] for i in range(len(li)))
    return sat

if __name__ == "__main__":
    assert sat(sol())
