def sat(li: List[int]):
    # Check if all elements in the list are either 2, 3, or 4 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    def sat(li: List[int]):
        return all(li[i] == li[i-1]*3 for i in range(1, len(li)))
    
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
