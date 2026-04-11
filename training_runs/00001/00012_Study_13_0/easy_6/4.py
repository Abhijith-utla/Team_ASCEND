def sat(x: float):
    return x > 3.1416

def sol():
    return 3.1416

# Test the solution
print(sat(sol()))  # Should return True
print(sat(sol()))  # Should return False

if __name__ == "__main__":
    assert sat(sol())
