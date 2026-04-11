def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    def sat(li: List[int]):
        return all(x + 1 == (2 ** x) - 1 for x in range(20))
    
    li = [x for x in range(20) if sat(li)]
    
    return len(li), li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
