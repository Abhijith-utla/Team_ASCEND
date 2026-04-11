def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sat(sol()))

# The function 'sat' checks if the first element of the list 'ls' is in the second element of the list 'ls'.
# If it is, and if it's not equal to the first element of the list 'ls', it returns True.
# If not, it returns False. 
# The function 'sol' creates a list and returns it.

# You can test the function with the following assertions:
assert sat(sol()) == False
assert sat(sol()[:-1]) == True
assert sat(sol()[1:]) == False
assert sat(sol()[:5] + [sol()[6]]) == True
assert sat(sol() + [sol()[1]]) == True
assert sat(sol() + [1, 2, 3, 4, 5]) == False

if __name__ == "__main__":
    assert sat(sol())
