def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 5 and s.count("1") == 1 and eval(s) == 295

def sol():
    return "8181818181"

# Testing the solution
if __name__ == "__main__":
    answer = sol()
    print(answer)
    assert sat(answer)

if __name__ == "__main__":
    assert sat(sol())
