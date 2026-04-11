def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63

def sol():
    return "81818"

print(sat(sol()))  # True

def sol():
    return "8218-"

print(sat(sol()))  # False

def sol():
    return "8181-"

print(sat(sol()))  # False

def sol():
    return "8/81818"

print(sat(sol()))  # False

def sol():
    return "8*81818"

print(sat(sol()))  # False

def sol():
    return "8+81818"

print(sat(sol()))  # False

def sol():
    return "8-81818"

print(sat(sol()))  # False

def sol():
    return "8181818"

print(sat(sol()))  # True

def sol():
    return "7181818"

print(sat(sol()))  # False

def sol():
    return "18181

if __name__ == "__main__":
    assert sat(sol())
