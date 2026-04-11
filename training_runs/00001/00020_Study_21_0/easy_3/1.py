def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3]

# The function sat() checks whether a list consists of exactly three unique elements. 
# If the list consists of exactly three unique elements, it returns True; otherwise, it returns False. 
# The assertion of sat(sol()) will confirm the output of sol() is a list with exactly three unique elements.

# If you want to check a different list, you can replace the line sol() with the list you want to test.

if __name__ == "__main__":
    assert sat(sol())
