def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    return [17, 3]

# The function 'sat' checks if either the number 17 appears zero times in a list or the number 3 appears zero times. If either condition is met, it returns a list containing 17 and 3.

if __name__ == "__main__":
    assert sat(sol())
