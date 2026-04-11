def sat(numbers: List[int], n=100):
    assert set(numbers) <= {0, 1}, 'Numbers must be in {0, 1}'
    assert len(numbers) >= n, 'Length of numbers must be greater than or equal to n'
    squares = {i ** 2: numbers[i] for i in range(1, len(numbers))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return {}

print(f'Solved: {sat([]) == False}')
print(f'Solved: {sat([1]*101) == False}')
print(f'Solved: {sat([0]*100 + [1]*1) == True}')
print(f'Solved: {sat([0]*99 + [1]*2 + [0]) == False}')
print(f'Solved: {sat([0]*100 + [1]*100) == True}')

if __name__ == "__main__":
    assert sat(sol())
