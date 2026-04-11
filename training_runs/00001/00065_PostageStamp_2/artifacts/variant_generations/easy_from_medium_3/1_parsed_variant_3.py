def sat(stamps):
    if len(stamps) > 0 and stamps[0] == 0:
        return False
    for s in stamps:
        assert s in [18, 1, 43, 81]
    return len(stamps) <= 1 and sum(stamps) == 3

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
