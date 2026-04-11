def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4] + [i for i in range(999)]
    return sat(li)

# This line is for checking the correctness of the solution. 
# If you want to remove this line, you can run the solution without checking.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
