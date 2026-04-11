def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456780')  # modifying the full set to test for more than 9 numbers
    for i in range(9):
        assert {x[i], x[i + 9], x[i + 18], x[i + 27], x[i + 36], x[i + 45], x[i + 54], x[i + 63], x[i + 72]} == full, "invalid row"
        assert {x[i + 9], x[i + 18], x[i + 27], x[i + 36], x[i + 45], x[i + 54], x[i + 63], x[i + 72], x[i + 81]} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
