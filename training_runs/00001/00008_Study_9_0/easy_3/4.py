def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

def sol():
    return [i for i in range(10) if ord(chr(i+65)) % 3 == 2]

print(sol())

# This function works by converting each character in the list to its ASCII value and checking if it is divisible by 3. It then sums up the values that are divisible by 3 to give a total. If the total is 0, it means all characters in the list are divisible by 3.

# Testing the function
def test():
    assert sat(sol())
test()

if __name__ == "__main__":
    assert sat(sol())
