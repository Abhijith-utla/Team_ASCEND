def sat(s: str):
    return s.count('s') == 300 and s.count('ss') == 301 and s.count('sss') == 298

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
