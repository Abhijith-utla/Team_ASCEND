def sat(quine: str):
    return eval(quine) == quine

def sol():
    return eval('sol')

print(sol())

# This will print: sol
# Because sol() is the same as its own evaluation, which is the same as the string 'sol'.

# This will also work:
# print(eval(repr(sol())))
# This will print: sol
# Because repr(sol()) converts the string 'sol' to a string that can be evaluated with eval.

if __name__ == "__main__":
    assert sat(sol())
