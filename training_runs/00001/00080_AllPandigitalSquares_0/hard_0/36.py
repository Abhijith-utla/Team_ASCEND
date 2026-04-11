def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return [sorted([int(s) for s in str(n * n)]) for n in set(range(10))] * 174

# The above code should solve the puzzle but it's incorrect because it's not checking if the list of integers is the same as a list of all numbers from 0 to 9 repeated 174 times.
# The correct code should be:
def sol():
    return [sorted([int(s) for s in str(n * n)]) for n in set(range(10))] * 174 == [list(range(10))] * 174

if __name__ == "__main__":
    assert sat(sol())
