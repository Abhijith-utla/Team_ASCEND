def sat(quine):
    return eval(quine[::-1]) == quine

def sol():
    return ""

# You can test this function with the following test case:
# assert sol() == ""
# assert sat(sol()) == True
# assert sol() != "a"
# assert sat(sol()) == False
# assert sol() == "a"
# assert sat(sol()) == True

if __name__ == "__main__":
    assert sat(sol())
