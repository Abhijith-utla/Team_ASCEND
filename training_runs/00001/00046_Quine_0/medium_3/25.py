def sat(quine):
    return eval(quine + "()")

def sol():
    return eval("""
    def sol():
        return {}
    """.format(str(sat)))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
