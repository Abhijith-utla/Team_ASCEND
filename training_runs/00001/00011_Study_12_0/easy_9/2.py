def sat(li: List[int]):
    li.insert(0, 5)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    return 5

# Checking if the function sat satisfies the condition
assert sat([])
!pip install numpy
!pip install sympy
!pip install matplotlib
!pip install scipy
!pip install pandas
!pip install sklearn
!pip install tensorflow
!pip install keras

if __name__ == "__main__":
    assert sat(sol())
