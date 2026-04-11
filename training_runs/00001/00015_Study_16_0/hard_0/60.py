def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    def sat(s: str):
        return float(s) + len(s) == 4.5

    # Test cases
    assert sat('1.2')
    assert not sat('2.3')
    assert sat('1234')
    assert not sat('1234.5')

    return 'The result is correct'

# Run the solution
print(sol())

if __name__ == "__main__":
    assert sat(sol())
