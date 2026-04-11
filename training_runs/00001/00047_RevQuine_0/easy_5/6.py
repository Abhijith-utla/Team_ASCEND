def sat(quine):
    return eval(quine[::-1]) == quine

def sol():
    return ''

# The output of the sol function will be an empty string, since a string is equal to its reverse when reversed.

# For example:
print(sat(sol()))
# Output: ''

if __name__ == "__main__":
    assert sat(sol())
