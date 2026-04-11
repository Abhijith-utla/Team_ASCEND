def sat(x: float):
    return x - 3.1415 == 123.456

def sol():
    return 123.456

# The function 'sat' takes a float parameter and returns True if the result is 123.456, False otherwise.
# This is done to satisfy the requirement of the problem. 
# Therefore, the function 'sol' returns 123.456 which is the correct answer to the problem.

if __name__ == "__main__":
    assert sat(sol())
