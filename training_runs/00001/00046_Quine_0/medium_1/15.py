def sat(quine):
    return eval(quine) == quine

def sol():
    return ''

# This will cause an assertion error as the quine is not defined
assert sat(sol()) 

# This will pass the assertion error
def quine():
    return """
    def sol():
        return ''

    print(sat(sol()))
    """
    assert sat(quine())

if __name__ == "__main__":
    assert sat(sol())
