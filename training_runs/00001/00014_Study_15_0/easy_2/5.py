def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

def sol():
    def sat(li: List[int]):
        return all(x >= 0 and x in range(20) for x in li)

    return sat([])

if __name__ == "__main__":
    assert sat(sol())
