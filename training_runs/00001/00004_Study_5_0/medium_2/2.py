def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(1, 11)])
    
    return sat

if __name__ == "__main__":
    assert sat(sol())
