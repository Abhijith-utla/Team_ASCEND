def sat(li: List[str]):
    return all(i.isdigit() for i in li)

def sol():
    def sat(li: List[str]):
        return all(i.isdigit() for i in li)
    return sat

if __name__ == "__main__":
    assert sat(sol())
