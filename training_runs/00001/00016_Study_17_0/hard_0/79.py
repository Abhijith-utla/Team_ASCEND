def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    def sat(i: int):
        return len(str(i + 1000)) > len(str(i + 1001))

    return sat

if __name__ == "__main__":
    assert sat(sol())
