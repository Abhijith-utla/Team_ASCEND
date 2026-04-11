def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [int(x) for x in input().split()]
    return sat(li)

# This function checks if the list satisfies the condition in the problem statement
def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

# This line is used to call the solution function and check if the result is correct
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
