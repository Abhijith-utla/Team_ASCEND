def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456780')  # modifying the full set to test for more than 9 numbers

def sol():
    return "_" * 35

def sat(x):
    assert all(c == "_" or c in set('123456780') for c in x)
    assert len(set(x)) == 10

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
