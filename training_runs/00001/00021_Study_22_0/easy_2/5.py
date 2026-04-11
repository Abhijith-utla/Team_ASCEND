def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

def sol():
    return '1234567890'

# Testing the solution
if sat(sol()):
    print("The solution is correct.")
else:
    print("The solution is incorrect.")

if __name__ == "__main__":
    assert sat(sol())
