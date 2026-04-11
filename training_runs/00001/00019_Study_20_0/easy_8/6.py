def sat(li: List[int]) -> bool:
    return all([j == 3 * i for j, i in enumerate(li)])

def sol():
    def sat(li: List[int]) -> bool:
        return all([j == 3 * i for j, i in enumerate(li)])
    
    return sat([])

# Uncomment this to test the solution with the provided test case
# print(sol() == True)

if __name__ == "__main__":
    assert sat(sol())
