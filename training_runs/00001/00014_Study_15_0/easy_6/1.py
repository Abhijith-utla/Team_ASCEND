def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

def sol():
    def sat(li: List[int]):
        for x in range(20):
            for y in li[:x + 1]:
                if y + x != 2 ** x:
                    return False
        return True

    return sat,

if __name__ == "__main__":
    assert sat(sol())
