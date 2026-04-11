def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456780')  # modifying the full set to test for more than 9 numbers

def sol():
    return "_"*30 + "1" + "_"*15 + "2" + "_"*15 + "3" + "_"*20 + "4" + "_"*15 + "5" + "_"*15 + "6" + "_"*15 + "7" + "_"*15 + "8" + "_"*15 + "9" + "_"*20 + "0" + "_"*15

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
