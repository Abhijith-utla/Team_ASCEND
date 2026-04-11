def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

def sol():
    def sat(li: list) -> bool:
        return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

    assert sat(list(range(10)))
    return

if __name__ == "__main__":
    assert sat(sol())
