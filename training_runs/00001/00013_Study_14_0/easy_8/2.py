def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    def sat(li: List[int]):
        return all([i == li[j] + li[j+1] for i in range(len(li))])
    return sat

if __name__ == "__main__":
    assert sat(sol())
