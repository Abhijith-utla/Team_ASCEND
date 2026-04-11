def sat(colors: List[int], n=0):
    # We only want to check if the colors list is of at least n length, 
    # and the ints in the list are in the set {0, 1}. 
    assert set(colors) <= {0, 1} and len(colors) >= n
    # We generate the dictionary squares with the numbers from 1 up to the length of the colors list. 
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    # We return True if there is any number i, j where i + j is a key in the squares dictionary 
    # and the corresponding value in squares is equal to the square of i + j. 
    return not any(c == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
