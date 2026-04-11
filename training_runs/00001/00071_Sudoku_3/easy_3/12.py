def sat(x: str, puz="_____42______7_____4______9__49___626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x)), "Mismatch in puzzle and answer"
    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    return True

def sol():
    return "429765816_381647925_162579483_678125493_254938167_916543782_825793146_394152678"

print(f"Your answer is: {sol()}")
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
