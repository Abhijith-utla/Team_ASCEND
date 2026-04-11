def sat(li):
    for i in li:
        for j in li:
            if abs(i - j) < 10:
                return False
    return len(li) == 100

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
