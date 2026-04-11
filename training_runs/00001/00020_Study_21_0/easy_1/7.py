def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

    return sat

if __name__ == "__main__":
    assert sat(sol())
