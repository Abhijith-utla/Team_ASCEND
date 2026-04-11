def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    li = [i % 2 for i in range(8)]  # generate a list with alternating 0s and 1s
    while not sat(li):  # keep changing the list until it satisfies the condition
        li[0] = (li[0] + 1) % 2
    return li

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

# Uncomment the following lines to check the result of the solution
# print(sol())
# print(sat(sol()))  # should return True

if __name__ == "__main__":
    assert sat(sol())
