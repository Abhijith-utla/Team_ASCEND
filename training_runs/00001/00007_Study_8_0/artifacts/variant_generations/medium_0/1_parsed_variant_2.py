def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
