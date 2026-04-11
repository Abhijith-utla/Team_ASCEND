def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine.strip()

def sol():
    rev_quine = """
    def sol():
        return \"""
        return eval(rev_quine) == rev_quine.strip()
        """
    return eval(rev_quine) == rev_quine.strip()

if __name__ == "__main__":
    assert sat(sol())
