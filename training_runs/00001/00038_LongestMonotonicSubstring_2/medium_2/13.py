def sat(x: List[int], length=737):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [1, 2, 3, 4, 5, 6, 7]

# Testing
if sat(sol()):
    print('The solution is correct.')
else:
    print('The solution is incorrect.')

if __name__ == "__main__":
    assert sat(sol())
