def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
