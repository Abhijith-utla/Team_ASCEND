def sat(x: str, puz="314869275_972561483_549782631_263514987_489765173_458731629_712894563_623514987_782631345_816249735_321978546_564129783_"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
