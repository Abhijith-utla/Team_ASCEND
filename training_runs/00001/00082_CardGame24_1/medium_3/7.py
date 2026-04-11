def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        'nums': [1, 10, 13, 4],
        'expr': '1+2*3-4/2'
    }

# Function to check if expression is valid
def check_expr(expr, nums):
    try:
        # Evaluate the expression
        result = eval(expr)
        # Check if the result is in the list of numbers
        if result in nums:
            return True
        else:
            return False
    except:
        return False

# Test the solution
solution = sol()
expr = solution['expr']
nums = solution['nums']
assert check_expr(expr, nums), "Expression is not valid"

if __name__ == "__main__":
    assert sat(sol())
