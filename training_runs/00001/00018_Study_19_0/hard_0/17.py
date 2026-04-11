def sat(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

def sol():
    li = [i for i in range(7)]  # Creating a list of integers from 0 to 6
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

if __name__ == "__main__":
    assert sat(sol())
